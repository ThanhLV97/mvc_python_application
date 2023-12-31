export const productServices = {
    search,
    getCategories
};

function search(product, category) {
    const requestOptions = {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ product, category })
    };
    return fetch('/api/products', requestOptions)
        .then(handleResponse)
        .then(products => {
            if (products) {
                localStorage.setItem('products', JSON.stringify(products));
            }
            return products;
        });
}

function getCategories() {
    const user = JSON.parse(localStorage.getItem('user'))
    const requestOptions = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${user.access_token}`
        },
    };
    return fetch('/api/categories', requestOptions)
        .then(handleResponse)
        .then(products => {
            if (products) {
                localStorage.setItem('products', products);
            }
            return products;
        });
}


function handleResponse(response) {
    return response.text().then(text => {
        const data = text && JSON.parse(text);
        if (!response.ok) {
            const error = (data && data.message) || response.statusText;
            return Promise.reject(error);
        }
        return data;
    });
}
