
task_input=document.querySelector('#task-input')

addbtn=document.getElementById('addbtn')
addbtn.addEventListener('click',function(){
    const ul=document.querySelector('#task-list')
    const li=document.createElement('li')
    li.innerText=task_input.value
    const libtn=document.createElement('button')
    libtn.innerText='delete'
    ul.appendChild(li)
    li.appendChild(libtn)
    libtn.addEventListener('click',function(){
        libtn.remove();
        li.remove()
    })

})


