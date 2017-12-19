$(function(){
	$('.hide-form').click(function () {
		switch ($('.hide-form').text()) {
			case 'Открыть окно создания треда':
				$('.hide-form').text('Закрыть окно создания треда')
				$('.form').css('display', 'block')
				break
			case 'Закрыть окно создания треда':
				$('.hide-form').text('Открыть окно создания треда')
				$('.form').css('display', 'none')
				break
			case 'Закрыть форму ответа':
				$('.hide-form').text('Открыть форму ответа')
				$('.form').css('display', 'none')
				break
			case 'Открыть форму ответа':
				$('.hide-form').text('Закрыть форму ответа')
				$('.form').css('display', 'block')
				break
		}
	})

	$('.hide-thread').on('click', function () {
		if ($(this).text() == 'Скрыть') {
			$(this).text('Показать')
			var spanSibs = $(this).siblings()
			$(spanSibs).eq(1).css('display', 'none')
			$(spanSibs).eq(2).css('display', 'none')
			titl = $(this).parent().siblings('.title').children('b').text()
			$(this).siblings('.name').after(' <b>' + titl + '</b>')
			$(this).parent().siblings().css('display', 'none')
			$(this).parent().parent().siblings().css('display', 'none')
		}
		else {
			$(this).text('Скрыть')
			var spanSibs = $(this).siblings()
			$(spanSibs).eq(2).css('display', 'inline')
			$(spanSibs).eq(3).css('display', 'inline')
			$(this).siblings('b').remove()
			$(this).parent().siblings().css('display', 'block')
			$(this).parent().parent().siblings().css('display', 'inline-block')
		}
	})
});