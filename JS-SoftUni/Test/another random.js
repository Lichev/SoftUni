function smallShop(city, product, quantity) {


  switch (city) {
    case "Sofia":
      switch (product) {
        case "coffee":
          console.log(quantity * 0.5);
          break;
        case "water":
          console.log(quantity * 0.8);
          break;
        case "beer":
          console.log(quantity * 1.2);
          break;
        case "sweets":
          console.log(quantity * 1.45);
          break;
        case "peanuts":
          console.log(quantity * 1.6);
          break;
      }
      break;

    case "Plovdiv":
      switch (product) {
        case "coffee":
          console.log(quantity * 0.4);
          break;
        case "water":
          console.log(quantity * 0.7);
          break;
        case "beer":
          console.log(quantity * 1.15);
          break;
        case "sweets":
          console.log(quantity * 1.3);
          break;
        case "peanuts":
          console.log(quantity * 1.5);
          break;
      }
      break;

    case "Varna":
      switch (product) {
        case "coffee":
          console.log(quantity * 0.45);
          break;
        case "water":
          console.log(quantity * 0.7);
          break;
        case "beer":
          console.log(quantity * 1.1);
          break;
        case "sweets":
          console.log(quantity * 1.35);
          break;
        case "peanuts":
          console.log(quantity * 1.55);
          break;
      }
      break;
  }
}
smallShop("Sofia", "coffee", "2");

/*
град  coffee	water	beer	sweets	peanuts
Sofia	0.50	 0.80	1.20	1.45	1.60
Plovdiv	0.40	0.70	1.15	1.30	1.50
Varna	0.45	0.70	1.10	1.35	1.55
*/
