let slides=document.querySelectorAll('.slide');
let index=0;
setInterval(()=>{
  slides.forEach(s=>s.classList.remove('active'));
  index=(index+1)%slides.length;
  slides[index].classList.add('active');
},3000);
document.querySelectorAll('.count').forEach(counter=>{
  let target=+counter.dataset.target;
  let c=0;
  let interval=setInterval(()=>{
    c++;
    counter.innerText=c;
    if(c==target) clearInterval(interval);
  },40);
});

