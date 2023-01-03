const text = document.querySelector('.text');
const txt = ["Welcome you all🍭🍭🍭. ", "  北极光之夜,夜越黑,星星越亮。", "  答案在风中飘荡🪁🪁🪁。"];
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