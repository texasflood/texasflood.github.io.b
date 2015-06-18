$(function () {
    var addInputRow = function () {
        $('#input').append($('#template').html());
    };

    addInputRow();
    $('#ActionAddRow').on('click', addInputRow);
    $('#ActionSubmit').on('click', function () {
        var data = $('#input tr').map(function () {
            var values = {};
            $('input', $(this)).each(function () {
                if (this.type === 'checkbox') {
                    values[this.name] = this.checked;
                } else {
                    values[this.name] = this.value;
                }
            });
            return values;
        }).get();
        $.post('/echo/json/', {
            json: JSON.stringify(data),
            delay: 1
        }).done(function (response) {
            alert("POST success");
            console.log(response);
        });
    });
});
