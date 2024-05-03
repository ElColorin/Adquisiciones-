const products = [
    {
      productName: "",
      price: 15,
      img: "",
      category: 'monitores'
    },
    {
      productName: "",
      price: 30,
      img: "",
      category: 'monitores'
    },
    {
      productName: "",
      price: 80,
      img: "",
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