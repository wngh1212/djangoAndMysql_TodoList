window.onload = function(){
    const checkbox = document.querySelector('.change')
const pwd = document.querySelector('.pwd')
checkbox.addEventListener('click',function(){
if(checkbox.checked){
    pwd.type = 'text'
}else{
    pwd.type = 'password'
}
})

}