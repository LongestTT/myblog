// 滑动
let i = true
const mySwitch = () => {
    if (i) {
        // 获取到滑动盒子的dom元素并修改它移动的位置
        $(".pre-box").css("transform", "translateX(100%)")
        // 获取到滑动盒子的dom元素并修改它的背景颜色
        $(".pre-box").css("background-color", "#c9e0ed")
        // 修改图片的路径
        $("img").attr("src", "https://liucy.fun/static/media/wuwu.jpeg")
        i = !i
    } else {
        $(".pre-box").css("transform", "translateX(0%)")
        $(".pre-box").css("background-color", "#edd4dc")
        $("img").attr("src", "https://liucy.fun/static/media/waoku.jpg")
        i = true
    }
}


const bubleCreate = () => {
    // 获取body元素
    const body = document.body
    // 创建泡泡元素
    const buble = document.createElement('span', '1')
    // 设置泡泡半径
    let r = Math.random() * 5 + 25 //半径大小为25~30
    // 设置泡泡的宽高
    buble.style.width = r + 'px'
    buble.style.height = r + 'px'
    // 设置泡泡的随机起点
    buble.style.left = Math.random() * innerWidth + 'px'
    // 为body添加buble元素
    body.append(buble)
    // 4s清除一次泡泡
    setTimeout(() => {
        buble.remove()
    }, 4000)
}
// 每200ms生成一个泡泡
setInterval(() => {
    bubleCreate()
}, 200);