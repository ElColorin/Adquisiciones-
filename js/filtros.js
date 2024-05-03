const products = [
    {
      productName: "Monitor Acer",
      price: 80,
      img: "https://i.blogs.es/61c495/pantalla/1366_2000.jpg",
      category: 'monitores'
    },
    {
      productName: "Monitor LG",
      price: 30000000,
      img: "https://cdn.grupoelcorteingles.es/SGFM/dctm/MEDIA03/202310/17/00115216121499____1__640x640.jpg",
      category: 'monitores'
    },
    {
      productName: "Honor 16gb ram ",
      price: 800000000,
      img: "https://media.gq.com.mx/photos/61e70ca3f4e647708c8d61cf/master/w_1600%2Cc_limit/HONOR%2520MagicBook%2520X%252015.jpg",
      category: 'compus'
    },
    {
      productName: "apple hd",
      price: 40,
      img: "https://media.gq.com.mx/photos/61e70ca25def32c5619cef06/16:9/w_1280,c_limit/Lenovo%20Yoga%20Slim%207%20Pro.jpg",
      category: 'compus'
    },
    {
      productName: "Monitor 22 Full HD",
      price: 50,
      img: "https://media.spdigital.cl/thumbnails/products/8zmbsuwe_a0a8d365_thumbnail_512.jpg",
      category: 'monitores'
    },
    {
      productName: "34gb",
      price: 60,
      img: "https://s1.eestatic.com/2018/06/07/actualidad/actualidad_313234074_130230320_1706x960.jpg",
      category: 'memorias ram'
    },
    {
      productName: "64 gb",
      price: 70,
      img: "https://media.kingston.com/kingston/features/ktc-feature-image-fury-beast-rgb-black-ddr4-lg.jpg",
      category: 'memorias ram'
    },
    {
      productName: "16gb",
      price: 20,
      img: "https://static6.depositphotos.com/1135132/669/i/450/depositphotos_6695663-stock-photo-high-performance-ddr3-ecc-computer.jpg",
      category: 'memorias ram'
    },
  ]
  
  const displayProducts = (productsToShow) => {
    const shopContent = document.getElementById("shopContent");
  
    shopContent.innerHTML = "";
    productsToShow.forEach(product => {
      const div = document.createElement("div");
      div.className = 'card-products';
      div.innerHTML = `
        <img src="${product.img}" alt="algun-alt">
        <h3>${product.productName}</h3>
        <p class="price"> $ ${product.price.toLocaleString()}</p> <!-- Aquí se utiliza toLocaleString() -->
        <button>Agregar al carrito</button>
      `;
      shopContent.append(div);
    })
  }
  
  const filterProducts = (category) => {
    const productsToShow = products.filter(product => product.category === category)
    displayProducts(productsToShow)
  }
  
  const ramBtn = document.getElementById('ramBtn');
  const monitoresBtn = document.getElementById('monitoresBtn');
  const compusBtn = document.getElementById('compusBtn');
  const todosBtn = document.getElementById('todosBtn');
  
  ramBtn.addEventListener('click', () => {
    filterProducts('memorias ram');
  });
  
  monitoresBtn.addEventListener('click', () => {
    filterProducts('monitores');
  });
  
  compusBtn.addEventListener('click', () => {
    filterProducts('compus');
  });
  
  todosBtn.addEventListener('click', () => {
    displayProducts(products)
  });
  
  displayProducts(products)