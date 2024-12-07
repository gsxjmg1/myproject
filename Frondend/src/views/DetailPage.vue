<template>
  <div class="container">
    <!-- 标题部分 -->
    <h1>{{ name }}</h1>

    <!-- 介绍文字 -->
    <div class="intro-text">
      <p class="main-intro">{{ introText }}</p>
    </div>

    <!-- 页面介绍文字和图片部分 -->
    <div class="content">
      <div v-for="(image, index) in imageList" :key="index" class="content-item">
        <div class="text-section">
          <p class="page-intro" >{{image.description}}</p>
        </div>
        <div class="image-section">
          <img :src="'http://localhost:8000/static/images/' + image.src + '?t=' + new Date().getTime()" :alt="`Image ${index + 1}`" class="detail-image" />
        </div>
      </div>
    </div>

    <!-- 返回主页面链接 -->
    <router-link to="/" class="back-link">返回主页面</router-link>
  </div>
</template>





<script>
import request from '../utils/reques'

export default {
  name: 'DetailPage',
  data() {
    return {
      name:'',
      id: this.$route.params.id,
      introText: '', // 页面介绍文字
      imageList: []
    }
  },
  watch: {
    // 监听路由参数的变化
    '$route.params.id': {
      handler(newId) {
        // 更新id并发起请求获取详细数据
        this.id = newId;
        this.fetchDetailData(newId);  // 调用方法获取详细数据
      },
      immediate: true  // 确保在初始化时也会执行一次handler
    }
  },
  methods: {
    fetchDetailData(id) {
      // 发起GET请求获取数据
      request.get(`/detail/${id}`)
        .then(response => {
          // 更新组件的data
          this.name = response.data.name;
          this.introText = response.data.intro;
          this.imageList = response.data.images;
          console.log(response);  // 打印返回的数据
        })
        .catch(error => {
          // 处理请求错误
          console.error('获取详情失败:', error);
        });
    }
  }
}
</script>

<style scoped>
/* 总容器样式 */
.container {
  width: 80%;
  margin: 0 auto;
  padding: 20px;
}

/* 标题部分 */
h1 {
  font-size: 50px;
  text-align: center;
  margin-bottom: 20px;
  color: white;
  text-shadow: 0 0 5px rgba(255, 140, 0, 0.8), 0 0 10px rgba(255, 165, 0, 0.5); /* 橙色光晕 */
}

/* 开头的介绍文字 */
.intro-text {
  margin-bottom: 30px;
}

.main-intro {
  font-size: 20px;
  color: white;
  text-align: justify;
  line-height: 1.6;
  text-indent: 2em;  /* 首行缩进 */
  text-shadow: 0 0 5px rgba(255, 140, 0, 0.8), 0 0 10px rgba(255, 165, 0, 0.5); /* 橙色光晕 */
}

.page-intro {
  font-size: 20px;
  color: #333333; /* 深灰色 */
  text-align: justify;
  line-height: 1.6;
  text-indent: 2em;  /* 首行缩进 */
}

/* 每一段内容的样式：文字+图片 */
.content {
  display: flex;
  flex-direction: column;
  gap: 30px;
  background-color: white;
  padding: 20px;
  border-radius: 16px;  /* 卡片圆角效果 */
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s ease, transform 0.3s ease; /* 添加平滑过渡效果 */
}

/* 每段内容项 */
.content-item {
  display: flex;
  align-items: center; /* 垂直居中 */
  justify-content: space-between;
  padding: 20px 0;
  border-bottom: 1px solid #eee;  /* 用下划线隔开每一段 */
}

/* 左侧文字部分 */
.text-section {
  flex: 1;
  margin-right: 20px;
}

/* 右侧图片部分 */
.image-section {
  flex: 1;
  display: flex;
  justify-content: center;  /* 水平居中 */
  align-items: center;  /* 垂直居中 */
}

/* 固定大小的图片样式（修改为fill来强制图片填充容器） */
.detail-image {
  width: 500px; /* 固定宽度 */
  height: 300px; /* 固定高度 */
  object-fit: fill; /* 拉伸图片填充容器 */
  border-radius: 8px; /* 圆角效果 */
}

/* 鼠标悬停时的卡片悬浮效果 */
.content-item:hover {
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2); /* 增强阴影效果 */
  transform: translateY(-5px); /* 卡片向上浮动 */
  transition: transform 0.3s ease, box-shadow 0.3s ease; /* 添加平滑过渡 */
}

/* 返回主页面链接样式 */
.back-link {
  display: block;
  text-align: center;
  margin-top: 40px;
  font-size: 18px;
  color: #007bff;
  text-decoration: none;
}

.back-link:hover {
  text-decoration: underline;
}



</style>
