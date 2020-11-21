ctrl_pressed = false
alt_pressed = false
shift_pressed = false
caps_pressed = false
scroll_pressed = false
num_pressed = false

function toggleBoolean(variable){
    if(variable)
        return false;
    else
        return true;
}
function press_shift(){
    //Light in Shift!!
    Lshift = document.getElementsByClassName('left-shift');
    Lshift[0].classList.toggle('shift-on');
    Rshift = document.getElementsByClassName('right-shift');
    Rshift[0].classList.toggle('shift-on');

    var keys = document.getElementsByClassName('letter');
    for (key in keys){
        try{
            keys[key].classList.toggle('uppercase');
        }
        catch
        {
        //console.log(keys[key]);
        }
    }
    var num = document.getElementsByClassName('num');
    for(i in num)
        try{
            num[i].classList.toggle('on');
        }
        catch{
            //none;
        }

    var extnd = document.getElementsByClassName('extn');
    for(i in extnd)
        try{
            //console.log(extnd[i]);
            extnd[i].classList.toggle('on');
        }
        catch{
            //none;
        }
    shift_pressed = toggleBoolean(shift_pressed);
}

function press_ctrl(){
    //Light in Ctrl!!
    document.getElementsByClassName('left-ctrl')[0].classList.toggle('ctrl-on');
    document.getElementsByClassName('right-ctrl')[0].classList.toggle('ctrl-on');
    ctrl_pressed = toggleBoolean(ctrl_pressed);
    //console.log(ctrl_pressed);
}

function press_alt(){
    //Light in Alt!!
    document.getElementsByClassName('left-alt')[0].classList.toggle('alt-on');
    document.getElementsByClassName('right-alt')[0].classList.toggle('alt-on');
    alt_pressed = toggleBoolean(alt_pressed);
    //console.log(alt_pressed);
}
function press_caps(){
    document.getElementsByClassName('capslock')[0].classList.toggle('func-on');
    var keys = document.getElementsByClassName('letter');
    for (key in keys){
        try{
            keys[key].classList.toggle('uppercase');
        }
        catch
        {
        //console.log(keys[key]);
        }
    }
    caps_pressed = toggleBoolean(caps_pressed);
    //console.log(caps_pressed);
}
function press_num(){
    document.getElementsByClassName('numlock')[0].classList.toggle('func-on');
    num_pressed = toggleBoolean(num_pressed);
    //console.log(num_pressed);
}
function press_scroll(){
    document.getElementsByClassName('scrllock')[0].classList.toggle('func-on');
    scroll_pressed = toggleBoolean(scroll_pressed);
    //console.log(num_pressed);
}
function press(key)
{
    var hold = [];
    if(ctrl_pressed)
        hold.push('ctrl');
    if(alt_pressed)
        hold.push('alt');
    if(shift_pressed)
        hold.push('shift');
    if(caps_pressed)
        hold.push('caps');
    if(num_pressed)
        hold.push('num');
    if(scroll_pressed)
        hold.push('scroll');
    //console.log(this.Text);
    //shift_pressed = toggleBoolean(shift_pressed);
    $.post('/key', {
        'key' : key.toLowerCase(),
        'hold' : hold
    });
}
function more()
{
    try{
        numpad = document.getElementsByClassName('numberpad');
        for(i in numpad)
            {
                numpad[i].classList.toggle('on');
            }
    }
    catch{
        //pass;
    }
    try{
        funcpad = document.getElementsByClassName('functionpad');
    for(i in funcpad)
        {
            funcpad[i].classList.toggle('on');
        }
    }
    catch{
        //pass;
    }
    document.getElementsByClassName('more')[0].classList.toggle('back');
}


function fullscreen_win(){
    //console.log("Full....");
    document.getElementsByClassName('fullscreen')[0].classList.toggle('fullscreen-off');
    if (document.fullscreenElement) {
      document.exitFullscreen().catch((err) => console.error(err))
    } else {
      document.documentElement.requestFullscreen();
    }
  }
const hehe = document.querySelectorAll('.letter');
hehe.forEach(el => el.addEventListener('click', event => {
    press(event.target.innerText);
}));
const hoho = document.querySelectorAll('.symbol');
hoho.forEach(el => el.addEventListener('click', event => {
    press(event.target.innerText);
}));
const haha = document.querySelectorAll('.function');
haha.forEach(el => el.addEventListener('click', event => {
    var _key = event.target.innerText;
    if(_key == 'num lock')
    press_num();
    else if(_key == 'scroll lock')
    press_scroll();
    else
    press(_key);
}));

