const tbl = document.getElementById('tbl')
const body = document.body

tbl.addEventListener("change" , () => {
    if(tbl.checked){
        body.style.backgroundColor = 'aqua'
    }else{
        body.style.backgroundColor = 'white'
    }
})
