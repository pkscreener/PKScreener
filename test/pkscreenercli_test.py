"""
    The MIT License (MIT)

    Copyright (c) 2023 pkjmesra

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""
import logging
import os
import sys
import builtins
from unittest.mock import patch
from unittest import mock

import pytest
from PKDevTools.classes.ColorText import colorText
from PKDevTools.classes.log import default_logger

from pkscreener import pkscreenercli
from pkscreener.globals import shutdown


# Mocking necessary functions or dependencies
@pytest.fixture(autouse=True)
def mock_dependencies():
    pkscreenercli.args.exit = True
    # pkscreenercli.args.download = False
    pkscreenercli.args.answerdefault = "Y"
    with patch("pkscreener.globals.main"):
        with patch("pkscreener.classes.Utility.tools.clearScreen"):
            yield


def patched_caller(*args, **kwargs):
    if kwargs is not None:
        userArgs = kwargs["userArgs"]
        maxCount = userArgs.options
        pkscreenercli.args.options = str(int(maxCount) - 1)
        if int(pkscreenercli.args.options) == 0:
            pkscreenercli.args.exit = True
    else:
        pkscreenercli.args.exit = True


# Positive test case - Test if pkscreenercli function runs in download-only mode
def test_pkscreenercli_download_only_mode():
    with patch("pkscreener.globals.main") as mock_main:
        with pytest.raises(SystemExit):
            pkscreenercli.args.download = True
            pkscreenercli.pkscreenercli()
            mock_main.assert_called_once_with(
                downloadOnly=True,
                startupoptions=None,
                defaultConsoleAnswer="Y",
                user=None,
            )


# Positive test case - Test if pkscreenercli function runs with cron interval
def test_pkscreenercli_with_cron_interval():
    pkscreenercli.args.croninterval = "3"
    with patch("pkscreener.globals.main", new=patched_caller) as mock_main:
        with patch(
            "PKDevTools.classes.PKDateUtilities.PKDateUtilities.isTradingTime"
        ) as mock_is_trading_time:
            mock_is_trading_time.return_value = True
            pkscreenercli.args.exit = False
            pkscreenercli.args.options = "2"
            with pytest.raises(SystemExit):
                pkscreenercli.pkscreenercli()
                assert mock_main.call_count == 2


# Positive test case - Test if pkscreenercli function runs without cron interval
def test_pkscreenercli_with_cron_interval_preopen():
    pkscreenercli.args.croninterval = "3"
    with patch("pkscreener.globals.main", new=patched_caller) as mock_main:
        with patch(
            "PKDevTools.classes.PKDateUtilities.PKDateUtilities.isTradingTime"
        ) as mock_is_trading_time:
            mock_is_trading_time.return_value = False
            with patch(
                "PKDevTools.classes.PKDateUtilities.PKDateUtilities.secondsBeforeOpenTime"
            ) as mock_secondsBeforeOpenTime:
                mock_secondsBeforeOpenTime.return_value = -3601
                pkscreenercli.args.exit = False
                pkscreenercli.args.options = "1"
                with pytest.raises(SystemExit):
                    pkscreenercli.pkscreenercli()
                    assert mock_main.call_count == 1


# Positive test case - Test if pkscreenercli function runs without any errors
def test_pkscreenercli_exits():
    with patch("pkscreener.globals.main") as mock_main:
        with pytest.raises(SystemExit):
            pkscreenercli.pkscreenercli()
            mock_main.assert_called_once()


def test_intraday_enabled():
    with patch(
        "PKDevTools.classes.PKDateUtilities.PKDateUtilities.isTradingTime"
    ) as mock_is_trading_time:
        with patch(
            "pkscreener.classes.ConfigManager.tools.restartRequestsCache"
        ) as mock_cache:
            with pytest.raises(SystemExit):
                pkscreenercli.args.intraday = "15m"
                mock_is_trading_time.return_value = False
                pkscreenercli.pkscreenercli()
                mock_cache.assert_called_once()


# Positive test case - Test if setupLogger function is called when logging is enabled
def test_setupLogger_logging_enabled():
    with patch("PKDevTools.classes.log.setup_custom_logger") as mock_setup_logger:
        with patch(
            "PKDevTools.classes.PKDateUtilities.PKDateUtilities.isTradingTime"
        ) as mock_is_trading_time:
            with pytest.raises(SystemExit):
                pkscreenercli.args.log = True
                pkscreenercli.args.prodbuild = False
                pkscreenercli.args.answerdefault = None
                mock_is_trading_time.return_value = False
                with patch("builtins.input") as mock_input:
                    pkscreenercli.pkscreenercli()
                    mock_setup_logger.assert_called_once()
                    assert default_logger().level == logging.DEBUG
                    mock_input.assert_called_once()


# Negative test case - Test if setupLogger function is not called when logging is disabled
def test_setupLogger_logging_disabled():
    with patch("PKDevTools.classes.log.setup_custom_logger") as mock_setup_logger:
        with patch(
            "PKDevTools.classes.PKDateUtilities.PKDateUtilities.isTradingTime"
        ) as mock_is_trading_time:
            mock_is_trading_time.return_value = False
            mock_setup_logger.assert_not_called()
            assert default_logger().level in (logging.NOTSET, logging.DEBUG)

def test_setupLogger_shouldNotLog():
    with patch("PKDevTools.classes.log.setup_custom_logger") as mock_setup_logger:
        pkscreenercli.setupLogger(False,True)
        mock_setup_logger.assert_not_called()
        assert 'PKDevTools_Default_Log_Level' not in os.environ.keys()

def test_setupLogger_LogFileDoesNotExist():
    try:
        filePath = pkscreenercli.logFilePath()
        os.remove(pkscreenercli.logFilePath())
    except:
        pass
    with patch("PKDevTools.classes.log.setup_custom_logger") as mock_setup_logger:
        with patch("pkscreener.pkscreenercli.logFilePath") as mock_file_path:
            mock_file_path.return_value = filePath
            pkscreenercli.setupLogger(True,True)
            mock_setup_logger.assert_called()

# Positive test case - Test if pkscreenercli function runs in test-build mode
def test_pkscreenercli_test_build_mode():
    with patch("builtins.print") as mock_print:
        pkscreenercli.args.testbuild = True
        pkscreenercli.pkscreenercli()
        mock_print.assert_called_with(
            colorText.BOLD
            + colorText.FAIL
            + "[+] Started in TestBuild mode!"
            + colorText.END
        )


def test_pkscreenercli_prodbuild_mode():
    with patch("pkscreener.pkscreenercli.disableSysOut") as mock_disableSysOut:
        pkscreenercli.args.prodbuild = True
        with pytest.raises(SystemExit):
            pkscreenercli.pkscreenercli()
            mock_disableSysOut.assert_called_once()
    try:
        import signal

        signal.signal(signal.SIGBREAK, shutdown)
        signal.signal(signal.SIGTERM, shutdown)
    except Exception:# pragma: no cover
        pass

def test_pkscreenercli_decorator():
    with patch("builtins.print") as mock_print:
        builtins.print = pkscreenercli.decorator(builtins.print)
        print("something")
        mock_print.assert_not_called()
        pkscreenercli.printenabled = True
        print("something else")
        mock_print.assert_called()

def test_pkscreenercli_disablesysout():
    originalStdOut = sys.stdout
    original__stdout = sys.__stdout__
    with patch("pkscreener.pkscreenercli.decorator") as mock_decorator:
        pkscreenercli.originalStdOut = None
        pkscreenercli.disableSysOut(disable=True)
        mock_decorator.assert_called()
        assert sys.stdout != originalStdOut
        assert sys.__stdout__ != original__stdout
    with patch("pkscreener.pkscreenercli.decorator") as mock_disabled_decorator:        
        pkscreenercli.disableSysOut(disable=False)
        mock_disabled_decorator.assert_not_called()
        assert sys.stdout == originalStdOut
        assert sys.__stdout__ == original__stdout
    with patch("pkscreener.pkscreenercli.decorator") as mock_disabled_decorator:        
        pkscreenercli.originalStdOut = None
        pkscreenercli.disableSysOut(input=False, disable=True)
        mock_disabled_decorator.assert_called()
        mock_disabled_decorator.call_count = 1

def test_pkscreenercli_warnAboutDependencies():
    with patch.dict("pkscreener.Imports", {"talib": False}):
        with patch("builtins.print") as mock_print:
            with patch("builtins.input") as mock_input:
                pkscreenercli.warnAboutDependencies()
                mock_print.assert_called()
                mock_print.call_count = 2
                mock_input.assert_not_called()
    with patch.dict("pkscreener.Imports", {"talib": False, "pandas_ta":False}):
        with patch("builtins.print") as mock_print:
            with patch("builtins.input") as mock_input:
                pkscreenercli.warnAboutDependencies()
                mock_print.assert_called()
                mock_print.call_count = 2
                mock_input.assert_called()
    with patch.dict("pkscreener.Imports", {"talib": True, "pandas_ta":True}):
        with patch("builtins.print") as mock_print:
            with patch("builtins.input") as mock_input:
                pkscreenercli.warnAboutDependencies()
                mock_print.assert_not_called()
                mock_input.assert_not_called()

def test_pkscreenercli_multiprocessing_patch():
    with patch("sys.platform") as mock_platform:
        mock_platform.return_value = "darwin"
        with patch("multiprocessing.set_start_method") as mock_mp:
            with pytest.raises((SystemExit)):
                pkscreenercli.pkscreenercli()
                mock_mp.assert_called_once_with("fork")
        
        mock_platform.return_value = "linux"
        with patch("sys.platform.startswith") as mock_platform_starts_with:
            mock_platform_starts_with.return_value = False
            with patch("multiprocessing.set_start_method") as mock_mp:
                with pytest.raises((SystemExit)):
                    pkscreenercli.pkscreenercli()
                    mock_mp.assert_not_called()

def test_pkscreenercli_clearscreen_is_called_whenstdOut_NotSet():
    with patch("pkscreener.classes.Utility.tools.clearScreen") as mock_clearscreen:
        with pytest.raises((SystemExit)):
            pkscreenercli.pkscreenercli()
            mock_clearscreen.assert_called_once()

def test_pkscreenercli_setConfig_is_called_if_NotSet():
    with patch("pkscreener.classes.ConfigManager.tools.checkConfigFile") as mock_chkConfig:
        mock_chkConfig.return_value = False
        with patch("pkscreener.classes.ConfigManager.tools.setConfig") as mock_setConfig:
            with pytest.raises((SystemExit)):
                pkscreenercli.pkscreenercli()
                mock_setConfig.assert_called_once()

def test_pkscreenercli_monitor_mode():
    with patch("builtins.print") as mock_print:
        with pytest.raises((SystemExit)):
            pkscreenercli.args.monitor = True
            pkscreenercli.pkscreenercli()
            mock_print.assert_called_with("Not Implemented Yet!")

def test_pkscreenercli_cron_std_mode_screening():
    with patch("pkscreener.pkscreenercli.scheduleNextRun") as mock_scheduleNextRun:
        with pytest.raises((SystemExit)):
            pkscreenercli.args.croninterval = 99999999
            pkscreenercli.args.download = False
            pkscreenercli.pkscreenercli()
            mock_scheduleNextRun.assert_called_once()

def test_pkscreenercli_std_mode_screening():
    with patch("pkscreener.pkscreenercli_x64.runApplication") as mock_runApplication:
        with pytest.raises((SystemExit)):
            pkscreenercli.pkscreenercli()
            mock_runApplication.assert_called_once()

def test_pkscreenercli_cron_std_mode_screening_with_no_schedules():
    with patch("PKDevTools.classes.PKDateUtilities.PKDateUtilities.isTradingTime") as mock_tradingtime:
        mock_tradingtime.return_value = True
        with patch("time.sleep") as mock_sleep:
            with patch("pkscreener.pkscreenercli_x64.runApplication") as mock_runApplication:
                with pytest.raises((SystemExit)):
                    pkscreenercli.args.croninterval = 99999999
                    pkscreenercli.args.exit = True
                    pkscreenercli.pkscreenercli()
                    mock_runApplication.assert_called_once()
                    mock_sleep.assert_called_once_with(3)

def test_pkscreenercli_cron_std_mode_screening_with_schedules():
    with patch("PKDevTools.classes.PKDateUtilities.PKDateUtilities.isTradingTime") as mock_tradingtime:
        mock_tradingtime.return_value = False
        with patch("time.sleep") as mock_sleep:
            with patch("pkscreener.pkscreenercli_x64.runApplication") as mock_runApplication:
                with patch("PKDevTools.classes.PKDateUtilities.PKDateUtilities.secondsAfterCloseTime") as mock_seconds:
                    mock_seconds.return_value = 3601
                    with pytest.raises((SystemExit)):
                        pkscreenercli.args.croninterval = 1
                        pkscreenercli.args.exit = True
                        pkscreenercli.args.download = False
                        pkscreenercli.pkscreenercli()
                        mock_sleep.assert_called_once_with(pkscreenercli.args.croninterval)
                        mock_runApplication.assert_called()
                with patch("PKDevTools.classes.PKDateUtilities.PKDateUtilities.secondsBeforeOpenTime") as mock_seconds:
                    mock_seconds.return_value = -3601
                    with pytest.raises((SystemExit)):
                        pkscreenercli.args.croninterval = 1
                        pkscreenercli.args.exit = True
                        pkscreenercli.args.download = False
                        pkscreenercli.pkscreenercli()
                        mock_sleep.assert_called_once_with(pkscreenercli.args.croninterval)
                        mock_runApplication.assert_called()

def test_pkscreenercli_workflow_mode_screening():
    with patch("pkscreener.pkscreenercli.disableSysOut") as mock_disableSysOut:
        with patch("pkscreener.pkscreenercli_x64.runApplication"):
            # run_once = mock.Mock(side_effect=[True, False])
            pkscreenercli.args.v = True
            pkscreenercli.args.monitor = False
            pkscreenercli.args.croninterval = None
            pkscreenercli.args.download = False
            pkscreenercli_x64.runApplicationForScreening()
            mock_disableSysOut.assert_called_with(disable=False)
            with pytest.raises((SystemExit)):
                # run_once = mock.Mock(side_effect=[True, False])
                pkscreenercli.args.v = False
                pkscreenercli_x64.runApplicationForScreening()
                mock_disableSysOut.assert_not_called()

def test_pkscreenercli_cron_mode_scheduling():
    with patch("PKDevTools.classes.PKDateUtilities.PKDateUtilities.isTradingTime") as mock_tradingtime:
        mock_tradingtime.return_value = False
        with patch("time.sleep") as mock_sleep:
            with patch("pkscreener.pkscreenercli_x64.runApplication") as mock_runApplication:
                with patch("PKDevTools.classes.PKDateUtilities.PKDateUtilities.secondsAfterCloseTime") as mock_seconds_after:
                    with patch("PKDevTools.classes.PKDateUtilities.PKDateUtilities.nextRunAtDateTime") as mock_nextRun:
                        mock_nextRun.return_value = "Test Next Run Schedule"
                        with patch("PKDevTools.classes.PKDateUtilities.PKDateUtilities.secondsBeforeOpenTime") as mock_seconds_before:
                            mock_seconds_after.return_value = 3601
                            mock_seconds_before.return_value = -3601
                            pkscreenercli.args.croninterval = 1
                            pkscreenercli.args.exit = True
                            pkscreenercli.args.download = False
                            with patch("pkscreener.globals.main") as mock_main:
                                pkscreenercli.scheduleNextRun()
                                # mock_sleep.assert_called_once_with(pkscreenercli.args.croninterval)
                                mock_runApplication.assert_called()
