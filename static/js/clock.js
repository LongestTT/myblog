const text = document.querySelector('.text');
const txt = ["Welcome you allð­ð­ð­. ", "  åæåä¹å¤,å¤è¶é»,ææè¶äº®ã", "  ç­æ¡å¨é£ä¸­é£è¡ðªðªðªã"];
let index = 0;
let xiaBiao = 0;
let huan = true;
setInterval(function () {
    if (huan) {
        text.innerHTML = txt[xiaBiao].slice(0, ++index);
    } else {
        text.innerHTML = txt[xiaBiao].slice(0, index--);
    }
    if (index == txt[xiaBiao].length + 3) {
        huan = false;
    } else if (index < 0) {
        index = 0;
        huan = true;
        xiaBiao++;
        if (xiaBiao >= txt.length) {
            xiaBiao = 0;
        }
    }
}, 200)