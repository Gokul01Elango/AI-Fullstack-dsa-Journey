/*
// Select by ID
document.getElementById('myId');

// Select by class (returns HTMLCollection)
document.getElementsByClassName('myClass');

// Select by tag (returns HTMLCollection)
document.getElementsByTagName('p');

// Select first match (CSS selector)
document.querySelector('.myClass');

// Select all matches (NodeList)
document.querySelectorAll('.myClass');

*/

// console.log(document.getElementById('tag1'))
// console.log(document.getElementsByClassName('para'))
// console.log(document.getElementsByTagName('p'))
// console.log(document.querySelector('.para'))
// console.log(document.querySelectorAll('.para'))

// document.querySelector('h1').innerText = "Hello Gokul!";
// document.querySelector('p').innerHTML = "<b>Bold Text</b>";

document.querySelector('h1').innerText = "Hello Gokul!";
document.querySelector('p').innerHTML = "<b>Bold Text</b>";


document.querySelector('.value').innerText="Admin block"


document.getElementById('greenbtn').addEventListener('click',function(){
    document.body.style.backgroundColor = 'green';
})
document.getElementById('redbtn').addEventListener('dblclick',function(){
    document.body.style.backgroundColor = 'red';
})
document.getElementById('bluebtn').addEventListener('mouseover',function(){
    document.body.style.backgroundColor='blue'
})

    document.getElementById('input').addEventListener('input',function(){
        let count=document.getElementById('input').value.length;
        document.getElementById('animation').innerHTML=`Typing...${count}`
    })
document.getElementById('input').addEventListener('pointerout',function(){
   
    document.getElementById('animation').innerHTML=count
    
})

// Create and delete Elements

const newdiv=document.createElement('div')
newdiv.textContent="Newly created"
document.body.appendChild(newdiv)
newdiv.remove();

// Create li inside the ul
const newul=document.getElementById('list')
const li=document.createElement('li')
li.textContent="list 1"
newul.appendChild(li)

// Create and add list into the page using button

btn=document.querySelector('#btn-add')
count=0
btn.addEventListener('click',function(){
        count++
        const ul=document.getElementById('list2')
        const li=document.createElement('li')
        li.textContent=`value ${count}`
        ul.appendChild(li)
})

