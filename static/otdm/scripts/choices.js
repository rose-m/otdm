(function () {
    /*
        We use an IIFE to properly encapsulate all JavaScript code and prevent
        leaking anything into global scope.
     */
    var table = jQuery('.otdm__choices-table');

    getAllRadios().on('click', function () {
        var input = jQuery(this);
        var selected = getRadioInfo(input);

        getAllRadios().each(function () {
            var radio = jQuery(this);
            var info = getRadioInfo(radio);
            if (info.name === selected.name) {
                return;
            }

            if (info.value === selected.value) {
                if (info.week < selected.week) {
                    radio.prop('checked', true);
                } else {
                    radio.prop('checked', false);
                }
            } else {
                if (info.week < selected.week) {
                    radio.prop('checked', false);
                } else {
                    radio.prop('checked', true);
                }
            }
        });
    });

    var clearHover;
    getAllLabels().hover(function () {
        if (clearHover) {
            clearTimeout(clearHover);
        }

        var label = jQuery(this);
        var input = label.find('> .otdm__choice-input');
        var selected = getRadioInfo(input);
        label.closest('td').addClass('highlight');

        getAllRadios().each(function () {
            var radio = jQuery(this);
            var info = getRadioInfo(radio);
            if (info.name === selected.name) {
                if (info.value !== selected.value) {
                    radio.closest('td').removeClass('highlight');
                }
                return;
            }

            if (info.value === selected.value) {
                if (info.week < selected.week) {
                    radio.closest('td').addClass('highlight');
                } else {
                    radio.closest('td').removeClass('highlight');
                }
            } else {
                if (info.week < selected.week) {
                    radio.closest('td').removeClass('highlight');
                } else {
                    radio.closest('td').addClass('highlight');
                }
            }
        });
    }, function () {
        clearHover = setTimeout(function () {
            getAllLabels().each(function () {
                jQuery(this).closest('td').removeClass('highlight');
            });
        }, 200);
    });

    function getAllRadios() {
        return table.find('.otdm__choice-input');
    }

    function getAllLabels() {
        return table.find('.otdm__choice-cell > label');
    }

    function getRadioInfo(radio) {
        var name = radio.attr('name');
        var value = radio.val();
        var week = parseInt(radio.data('week'));
        return {
            name: name,
            value: value,
            week: week,
        };
    }
}());
