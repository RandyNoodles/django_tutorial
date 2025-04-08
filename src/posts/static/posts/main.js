

const hwBox = document.getElementById("hello-world");

$.ajax({
    type: 'GET',
    url: '/hello-world/',
    success: function(response){
        console.log('success', response)
        hwBox.textContent = response.text;
    },
    error: function(error){
        console.log(error)
    }
})