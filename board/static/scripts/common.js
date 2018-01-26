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
				$('.reply-adding').attr('class', 'disable reply-adding bttn')
				break
			case 'Открыть форму ответа':
				$('.hide-form').text('Закрыть форму ответа')
				$('.form').css('display', 'block')
				$('.reply-adding').attr('class', 'reply-adding bttn')
				break
		}
	})

	$('.hide-thread').on('click', function () {
		if ($(this).text() == 'Скрыть') {
			$(this).text('Показать')
			var spanSibs = $(this).siblings()
			$(spanSibs).eq(1).css('display', 'none')
			$(spanSibs).eq(2).css('display', 'none')
			titl = $(this).parent().siblings().eq(0).children('.title').children().text()
			$(this).siblings('.name').after(' <b>' + titl + '</b>')
			$(this).parents('.op').siblings().css('display', 'none')
			$(this).parents('td').siblings().css('display', 'none')
			$(this).parent().next().css('display', 'none')
		}
		else {
			$(this).text('Скрыть')
			var spanSibs = $(this).siblings()
			$(spanSibs).eq(2).css('display', 'inline')
			$(spanSibs).eq(3).css('display', 'inline')
			$(this).siblings('b').remove()
			$(this).parents('.op').siblings().css('display', 'inline-block')
			$(this).parents('.op').siblings('.missed').css('display', 'block')
			$(this).parent().siblings().css('display', 'block')
			$(this).parent().parent().siblings().css('display', 'inline-block')
		}
	})

	if ($('.errorlist').html() != undefined) {
		$('.hide-form').trigger('click')
	}

	$('.reply-adding').click(function (){
		if ($('form label').eq(3).text() == '') {
			$('form label').eq(3).text('Ответы:')
			var td = $('form label').eq(3).parent().next()
			$(td).append('<div class="input-like" style="min-height: 26px;"></div>')
			replyInput = $(td).find('div')
			fullNum = ''
		}
		replyNum = $(this).parent().children().eq(1).text().slice(1)
		fullNum += replyNum + ' '
		$(replyInput).append('<span class="reply-input">' + 
			replyNum + ' <span class="reply-delete">×</span>'
		)
		$(replyInput).find('.reply-delete').click(function () {
			var replyText = $(this).parent().text()
			var replyNum = replyText.slice(0, replyText.length-2)
			divChildren = $(this).parent().parent().children()
			if (divChildren.length == 1) {
				$('form label').eq(3).text('')
				$(replyInput).remove()
				$('#id_replies').val('')
			}
			else {
				inpValue = $('#id_replies').val()
				replacedValue = inpValue.replace(replyNum + ' ', '') 
				$('#id_replies').val(replacedValue)
			}
			$(this).parent().remove()
			$('#' + replyNum + ' p .reply-adding').attr('style', '')
		})
		$(this).css('display', 'none')
		$('#id_replies').val(fullNum)
	})
})