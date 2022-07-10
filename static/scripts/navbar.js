
function openMenu(){
    document.getElementById('navbar2').style.display="flex";
    document.getElementById('navbar').style.display="none";
    document.getElementById('close').style.display="flex";
    document.getElementById('open').style.display="none";
}

function closeMenu(){
    document.getElementById('navbar2').style.display="none";
    document.getElementById('navbar').style.display="flex";
    document.getElementById('close').style.display="none";
    if(screen.width >750){
        document.getElementById('open').style.display="none";
        
    }
    else{
        document.getElementById('open').style.display="flex";
        
    }
}
