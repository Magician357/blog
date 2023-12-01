const elements = document.querySelectorAll('*');
window.addEventListener('load', function () {
    console.log("loaded");
    elements.forEach(element=>{
        element.classList.add("loaded");
    })
})