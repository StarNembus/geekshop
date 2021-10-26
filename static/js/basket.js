window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function () {
        let t_href = event.target;
        console.log(t_href.name); // basket_id
        console.log(t_href.value) // basket_quantity

        $.ajax({ // сюда приходит result из basket/views.py
            url: '/baskets/edit/' + t_href.name + '/' + t_href.value + '/', // указываем клиенту куда нужно направить данные
            success: function (data) { // данные JsonResponse({'result': result})
                $('.basket_list').html(data.result); // замена данных на basket_list
            },
        })
    });
}