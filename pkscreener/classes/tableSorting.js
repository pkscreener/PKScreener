window.addEventListener('load', function() {
  if (document.getElementsByTagName("TR")[1].firstElementChild.innerText === 'Stock') {
    /*Get rid of the first row with Stocks on all columns*/
    document.getElementsByTagName("TR")[1].remove()
  }
  const getCellValue = (tr, idx) => tr.children[idx].innerText || tr.children[idx].textContent;
  const parsedNumber = (v) => parseFloat(v.replaceAll("/",""))
  const parsedInstanceCount = (v) => parseFloat(v.replaceAll("/","").split('(')[1].split(')')[0]);
  const percentDiff = (v1,v2) => parsedNumber(v1) - parsedNumber(v2)
  const countDiff = (v1,v2) => parsedInstanceCount(v1) - parsedInstanceCount(v2)
  const parsedInstanceCountAndNumber = (v1,v2) => countDiff(v1,v2) == 0 ? percentDiff(v1,v2) : countDiff(v1,v2)
  const chkBox = document.getElementById('chkActualNumbers')
  const comparer = (idx, asc) => (a, b) => ((v1, v2) => 
      v1 !== '' && v2 !== '' && !isNaN(parseFloat(v1)) && !isNaN(parseFloat(v2)) ? ((chkBox && chkBox.checked && v1.split('(').length > 1)? parsedInstanceCountAndNumber(v1,v2):percentDiff(v1,v2)): v1.toString().localeCompare(v2)
      )(getCellValue(asc ? a : b, idx), getCellValue(asc ? b : a, idx));

  // do the work...
  document.querySelectorAll('th').forEach(th => th.addEventListener('click', (() => {
      var table = th.closest('table');
      const tbody = table.querySelector('tbody');
      Array.from(tbody.querySelectorAll('tr'))
          .sort(comparer(Array.from(th.parentNode.children).indexOf(th), this.asc = !this.asc))
          .forEach(tr => tbody.appendChild(tr) );
  })));

  document.querySelectorAll('table tr td').forEach(function(e, i) {
    if (e.textContent.trim().length == 0 || e.textContent.trim() == "NaN") { // if row is empty which means the report did not get generated
        // e.parentNode.remove();
        e.textContent = "-"
    }
  });
})
const searchReportsByAny = () => {
  const trs = document.querySelectorAll('#resultsTable tr:not(.header)')
  const filter = document.querySelector('#searchReports').value
  const regex = new RegExp(filter, 'i')
  const isFoundInTds = td => regex.test(td.innerHTML)
  const isFound = childrenArr => childrenArr.some(isFoundInTds)
  const setTrStyleDisplay = ({ style, children }) => {
    style.display = isFound([
      ...children // <-- All columns
    ]) ? '' : 'none' 
  }
  trs.forEach(setTrStyleDisplay)
}
