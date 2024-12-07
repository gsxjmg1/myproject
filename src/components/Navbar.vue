<template>
  <div class="navbar">
    <div class="navbar-left">
      <a href="http://iisscs.aia.hust.edu.cn/index.htm"><img src="@/assets/logo.png" alt="Logo" class="logo"></a>
    </div>

    <div class="navbar-right">
      <ul id="nav">
        <li @click="navigateToPage('/')">
          <a href="#">主页面</a>
        </li>
        <li @click="navigateToPage('external')">
          <a href="#">实验室主页</a>
        </li>
        <li @click="navigateToPage('1')">
          <a href="#">异常检测</a>
        </li>
        <li @click="navigateToPage('2')">
          <a href="#">失效分析</a>
        </li>
        <li @click="navigateToPage('3')">
          <a href="#">知识图谱</a>
        </li>
        <li @click="navigateToPage('4')">
          <a href="#">数据采集</a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Navbar',
  data() {
    return {
    }
  },
  methods: {
  navigateToPage(page) {
    const currentRoutePath = this.$route.path;
    
    if (page === 'external') {
      window.open('http://iisscs.aia.hust.edu.cn/index.htm', '_blank');
    } else if (page === '/') {
      // 如果不是已经在根路径，则进行跳转
      if (currentRoutePath !== '/') {
        this.$router.push({ path: '/' });
      }
    } else {
      // 对于命名路由，需要检查路由名称和参数
      const targetRouteName = 'DetailPage';
      const targetRouteParams = { id: page };
      
      if (this.$route.name !== targetRouteName || JSON.stringify(this.$route.params) !== JSON.stringify(targetRouteParams)) {
        this.$router.push({ name: targetRouteName, params: targetRouteParams });
      }
    }
  }
}
}
</script>

<style scoped>
.navbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-image: url('../assets/background.jpg');
  padding: 10px 20px;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 50px;
  z-index: 1000;
}

.navbar-left {
  display: flex;
  align-items: center;
}

.logo {
  height: 50px;
  margin-right: 10px;
}


/* 去掉列表的点并将列表设置为水平 */
#nav {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    justify-content: space-around; /* 如果希望列表项之间有均匀的空间 */
    font-size: 15px; /* 调整字体大小 */
}

/* 移除a标签的默认样式，并为悬停效果做准备 */
#nav a {
    text-decoration: none; /* 移除默认下划线 */
    position: relative; /* 使伪元素相对定位 */
    padding: 15px 15px; /* 调整上下内边距以适应横线，并增加左右内边距以扩展间距 */
    display: inline-block; /* 确保伪元素正确地相对于链接文本定位 */
    font-size: inherit; /* 继承父元素的字体大小 */
    color: white;
    font-weight: bold; /* 加粗字体 */
}

/* 默认情况下不显示横线 */
#nav a::before,
#nav a::after {
    content: '';
    position: absolute;
    left: 0;
    width: 100%;
    height: 1px; /* 横线高度 */
    background-color: transparent; /* 初始颜色透明 */
    transition: background-color 0.3s ease; /* 添加过渡效果 */
}

/* 上方横线 */
#nav a::before {
    top: 0;
}

/* 下方横线 */
#nav a::after {
    bottom: 0;
}

/* 当鼠标悬停时改变横线的颜色 */
#nav a:hover::before,
#nav a:hover::after {
    background-color: white; /* 悬停时横线颜色 */
}
</style>
