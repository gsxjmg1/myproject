<template>
  <div>
      <!-- 轮播图 -->
      <el-carousel :interval="2000" arrow="always">
          <el-carousel-item v-for="item in carouselItems" :key="item.id">
            <img :src="'http://localhost:8000/static/images/' + item.imageSrc + '?t=' + new Date().getTime()" alt="Carousel Image" class="carousel-image">
          </el-carousel-item>
      </el-carousel>
      <!-- 实验室文字介绍 -->
      <div class="introduction">
        <h3 style="color:white">实验室简介</h3>
        <p style="color:white">工业互联网及系统安全实验室面向技术前沿和国家重大需求，围绕工业控制系统及其基础设施的信息安全防护，系统性地研究基于人工智能和大数据的主动安全防护技术，</p>
        <p style="color:white">为未来工业互联网和工业控制系统提供安全运行的解决方案。实验室现有专职教师3人，在读博士研究生9人，在读硕士研究生28人。</p>
      </div>
      <!-- 卡片 -->
      <div>
        <el-row :gutter="20">
          <el-col :span="6" v-for="card in cards" :key="card.id">
            <div class="card">
              <router-link :to="{ name: 'DetailPage', params: { id: card.id } }">
                <img :src="'http://localhost:8000/static/images/' + card.home_image" :alt="card.page_name" />
              </router-link>
              <p></p>
              <h1>{{ card.page_name }}</h1>
            </div>
          </el-col>
        </el-row>
      </div>
  </div>
</template>

<script>
import Navbar from '../components/Navbar.vue'
import request from '../utils/reques'

export default {
  name: 'HomeView',
  data(){
    return{
      carouselItems: [],
      cards: []
    }
  },
  components: {
    Navbar,
  },
  created(){
    request.get('/home/1')
      .then(response => {
        this.cards = response.data.data
      })
      .catch(error => {
        // 处理错误
        console.error('获取用户列表失败:', error);
      });
    request.get('/home/2')
      .then(response => {
        this.carouselItems = response.data.data
      })
      .catch(error => {
        // 处理错误
        console.error('获取用户列表失败:', error);
      });
  },
}
</script>

<style>
.el-carousel__container {
  position: relative;
  height: 550px;
}

.carousel-image {
  width: 100%;
  height: 100%;
  object-fit: cover; /* 或 contain */
}

/* 单个卡片样式 */
.card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center; /* 确保内容垂直居中 */
  width: 100%; /* 使用栅格系统的宽度 */
  max-width: 350px; /* 设置最大宽度 */
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 20px;
  box-sizing: border-box; /* 包含内边距计算宽度 */
  transition: transform 0.3s ease;
  margin-bottom: 20px; /* 调整卡片之间的上下间距 */
  background-color: rgb(237, 238, 241);
}

.card img {
  width: 100%;           /* 宽度设置为100%，适应卡片宽度 */
  height: 200px;         /* 设置固定高度 */
  object-fit: cover;     /* 裁剪图片以适应容器 */
  border-radius: 8px;    /* 圆角 */
  margin-bottom: 10px;   /* 图片与标题之间的间距 */
}

.card:hover {
  transform: translateY(-5px); /* 鼠标悬停时的轻微动画效果 */
}

.card h1 {
  margin-top: 0;         /* 移除顶部外边距以避免额外空间 */
  font-size: 24px;       /* 调整字体大小 */
  color: #4c74ba; /* 深蓝紫色字体 */
  text-align: center;    /* 文字居中 */
  line-height: 1.5;      /* 行高，增加行间距 */
  max-width: 90%;        /* 限制最大宽度 */
}

</style>