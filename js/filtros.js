const products = [
    {
      productName: "Monitor Acer",
      price: 15,
      img: "https://i.blogs.es/61c495/pantalla/1366_2000.jpg",
      category: 'monitores'
    },
    {
      productName: "Monitor LG",
      price: 30,
      img: "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.lg.com%2Fcl%2Fmonitores%2Ffhd-y-qhd%2F&psig=AOvVaw32RgWDywN1yYMFCbBbdOy4&ust=1714783300086000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCPDpuN2f8IUDFQAAAAAdAAAAABAM",
      category: 'monitores'
    },
    {
      productName: "Monitor 22 Full HD",
      price: 80,
      img: "https://www.google.com/url?sa=i&url=https%3A%2F%2Ftic-online-store.cl%2Fproducto%2Fsamsung-2%2F&psig=AOvVaw32RgWDywN1yYMFCbBbdOy4&ust=1714783300086000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCPDpuN2f8IUDFQAAAAAdAAAAABAU",
      category: 'compus'
    },
    {
      productName: "",
      price: 40,
      img: "",
      category: 'compus'
    },
    {
      productName: "",
      price: 50,
      img: "",
      category: 'monitores'
    },
    {
      productName: "",
      price: 60,
      img: "",
      category: 'memorias ram'
    },
    {
      productName: "",
      price: 70,
      img: "",
      category: 'memorias ram'
    },
    {
      productName: "",
      price: 20,
      img: "https://static6.depositphotos.com/1135132/669/i/450/depositphotos_6695663-stock-photo-high-performance-ddr3-ecc-computer.jpg",
      category: 'memorias ram'
    },
  ]
  
  const displayProducts = (productsToShow) => {
    const shopContent = document.getElementById("shopContent")
  
    shopContent.innerHTML = ""
    productsToShow.forEach(product => {
      const div = document.createElement("div")
      div.className = 'card-products'
      div.innerHTML = `
        <img src="${product.img}" alt="algun-alt">
        <h3>${product.productName}</h3>
        <p class="price"> $ ${product.price}</p>
        <button>Agregar al carrito</button>
      `
      shopContent.append(div)
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