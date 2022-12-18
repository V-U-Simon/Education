basketValues = {
    total_price: 0,
    total_count: 0,
    // 1: { id: 1, name: "product 1", price: 30, count: 2 },
}

const basketShowToggleEl = document.querySelector('.basketIconWrap')
const basketEl = document.querySelector('.basket')
const basketAddEl = document.querySelector('.basket')
const basketHeader = document.querySelector('.basketHeader')
const basketTotalPrice = document.querySelector('.basketTotalValue')
const basketTotalCount = document.querySelector('.basketIconWrap > span')


// show basket
basketShowToggleEl.addEventListener('click', () => basketEl.classList.toggle('hidden'))

// add to basket
document.querySelector('.featuredItems').addEventListener('click', (event) => {
    // проверяем место клика (по кнопке, или по картинке кнапки)
    if (!event.target.closest('button')) {
        return;
    }
    const productEl = event.target.closest('.featuredItem')
    console.log(productEl.dataset)
    id = productEl.dataset.id
    name_ = productEl.dataset.name
    price = +productEl.dataset.price

    // populate basket
    if (!basketValues[id]) {
        basketValues[id] = {id: id, name: name_, price: price, pricePerOne: price, count: 1}
        addToBasket(basketValues[id])
    } else {
        basketValues[id].price = basketValues[id].price + price
        basketValues[id].count = basketValues[id].count + 1
        updateToBasket(basketValues[id])
    }

    // update total_values
    basketValues.total_price += price 
    basketValues.total_count += 1 
    basketTotalPrice.textContent = basketValues.total_price
    basketTotalCount.textContent = basketValues.total_count
})


function addToBasket (product) {
    basketHeader.insertAdjacentHTML('afterend', `
    <div class="basketRow" data-id="${product.id}">
        <div>${product.name}</div>
        <div>${product.count}</div>
        <div>${product.pricePerOne}</div>
        <div>${product.price}</div>
    </div>
    `)
}

function updateToBasket (product) {
    document.querySelector(`.basketRow[data-id="${product.id}"]`).innerHTML = `
        <div>${product.name}</div>
        <div>${product.count}</div>
        <div>${product.pricePerOne}</div>
        <div>${product.price}</div>
    `
}

