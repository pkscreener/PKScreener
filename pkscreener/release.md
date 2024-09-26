[![MADE-IN-INDIA](https://img.shields.io/badge/MADE%20WITH%20%E2%9D%A4%20IN-INDIA-orange?style=for-the-badge)](https://en.wikipedia.org/wiki/India) [![GitHub release (latest by date)](https://img.shields.io/github/v/release/pkjmesra/PKScreener?style=for-the-badge)](#) [![GitHub all releases](https://img.shields.io/github/downloads/pkjmesra/PKScreener/total?color=Green&label=Downloads&style=for-the-badge)](#) [![MADE_WITH](https://img.shields.io/badge/BUILT%20USING-PYTHON-yellow?style=for-the-badge&logo=python&logoColor=yellow)](https://www.python.org/)

## What's New?
1. [v0.45.20240925.588] release
* Find a stock in scanners. You can now look-up a stock and find out which all basic standard scanners gave out that stock in result.
* GPU enabled for running scans on computers where GPU device(s) is available
* Excel hyperlinks enabled for stocks when the results are saved/exported to excel.
* Added support for time-window-slider. It's still an experimental feature. So use wth care. It may be buggy and may not work for all period/duration combinations. If you want to try this experimental feature, choose option 3 to go back in time and run the scan again to come up with a diff of stocks between now and then, when presented with options after the scan finishes. Please report various bugs under https://github.com/pkjmesra/PKScreener/issues
* Added more profitable setups. Try X > 12 > 33. Added Bullish Today for Previous Day Open/Close (PDO/PDC) with 1M Volume (Try X > 12 > 33 > 2) and moved the previous option under X > 12 > 33 > 1
* Added the ability to run VCP using additional filters. By default these filters are turned on but you can turn it off when running locally as well. Try X > 12 > 7 > 4
* Added two more piped scans with VCP/Volume/Price breakouts.
* Enabling entering specific date in YYYY-MM-DD format for quick backtests using T > B menu.
* Price action option added for filtering out stocks where price has crossed given SMA/EMA from above/below. Try X > 12 > 40
* Improved super-confluence. Added it under pre-defined scans as well. Try out P_1_26 and P_1_27.
* Short sell analysis options added : Try out X > 14 > 35 or X > 14 > 36 or X > 12 > 37 or X > 12 > 38.
* Added IPO-Lifetime First day bullish break. Try X > 13 > 39.
* Added several new sectoral indices. Try X > S >
* Fixed multiple bugs.

## Older Releases
* [https://github.com/pkjmesra/PKScreener/releases] : Discarded to save on storage costs!

## Downloads
| Operating System                                                                                         | Executable File                                                                                                                                                                                                               |
| -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white) | **[pkscreenercli.exe](https://github.com/pkjmesra/PKScreener/releases/download/0.45.20240925.588/pkscreenercli.exe)**                                                                                                         |
| ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)       | **[pkscreenercli.bin](https://github.com/pkjmesra/PKScreener/releases/download/0.45.20240925.588/pkscreenercli.bin)**                                                                                                         |
| ![Mac OS](https://img.shields.io/badge/mac%20os-D3D3D3?style=for-the-badge&logo=apple&logoColor=000000)  | **[pkscreenercli.run](https://github.com/pkjmesra/PKScreener/releases/download/0.45.20240925.588/pkscreenercli.run)** ([Read Installation Guide](https://github.com/pkjmesra/PKScreener/blob/main/INSTALLATION.md#for-macos)) |

## How to use?

[**Click Here**](https://github.com/pkjmesra/PKScreener) to read the documentation. You can also read it at https://pkscreener.readthedocs.io/en/latest/?badge=latest

## Join our Community Discussion

[**Click Here**](https://github.com/pkjmesra/PKScreener/discussions) to join the community discussion and see what other users are doing!

## Facing an Issue? Found a Bug?

[**Click Here**](https://github.com/pkjmesra/PKScreener/issues/new/choose) to open an Issue so we can fix it for you!

## Want to Contribute?

[**Click Here**](https://github.com/pkjmesra/PKScreener/blob/main/CONTRIBUTING.md) before you start working with us on new features!

## Disclaimer:
* DO NOT use the result provided by the software solely to make your trading decisions.
* Always backtest and analyze the stocks manually before you trade.
* The Author(s) and the software will not be held liable for any losses.

## License
* MIT: https://github.com/pkjmesra/PKScreener/blob/main/LICENSE
