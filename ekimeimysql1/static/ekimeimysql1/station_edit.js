//YouTubeジャンプ
$('.youtube-jump').on('click', function() {
	time = $(this).prev('.start_time').val()
	console.log(time)
	player.playVideo();
	player.seekTo(TimetoSecond(time), true);
})

function TimetoSecond(time) {
	t = time.split(':');
	hour = parseInt(t[0]) * 3600;
	minute = parseInt(t[1]) * 60;
	second = parseInt(t[2]);
	return hour + minute + second;
}

//曲・ボーカル追加
function add_song(name, pk) {
	var select = $('select.part_song')[0];
	var option = document.createElement('option');
	option.setAttribute('value', pk);
	option.innerHTML = name;

	select.add(option, 0);
	select.options[0].selected = true;
}

function add_vocal(name, pk) {
	var select = $('select.part_vocal')[0];
	var option = document.createElement('option');
	option.setAttribute('value', pk);
	option.innerHTML = name;

	select.add(option, 0);
	select.options[0].selected = true;
}

// 都道府県を選択したときの挙動
$('#pref-select').children('div').on('click', function() {
	pref = $(this).attr('value');
	var s = "http://localhost:8000/ekimeimysql1/api/line/" + pref + "/?format=json";
	$(".pref-line-select").empty();
	$.getJSON(s, function(data) {
		for (var i in data) {
			var op_line = "<div value='" + data[i].line_service_pk + "' class='line-option'>" + data[i].__str__ + "</div>";
			$(".pref-line-select").append(op_line);
		}
	})
})

// 事業者名を選択したときの挙動
$('#company-select').children('div').on('click', function() {
	company = $(this).attr('value');
	var s = "http://localhost:8000/ekimeimysql1/api/company/" + company + "/?format=json";
	$(".company-line-select").empty();
	$.getJSON(s, function(data) {
		for (var i in data) {
			var op_line = "<div value='" + data[i].line_service_pk + "' class='line-option'>" + data[i].__str__ + "</div>";
			$(".company-line-select").append(op_line);
		}
	})
})

//路線を選択した時の挙動
$(document).on('click', '.line-option', function() {
	line = $(this).attr("value");
	var s = "http://localhost:8000/ekimeimysql1/api/stationservice/" + line + "/?format=json";
	$('.station-select').empty();
	$.getJSON(s, function(data) {
		for (var i in data) {
			var op_station = "<option value='" + data[i].station_service_pk + "' data-name='" + data[i].__str__ + "' data-line='" + data[i].line_service_name + "' class='station-option'>" + data[i].__str__ + "</option>"
			$(".station-select").append(op_station);
		}
	})
})

//逆順にした時の挙動
$(document).on('click', '.station-reverse', function() {
	var list = $('.station-option').toArray().reverse();
	$('.station-select').empty().append(list);
})

//乗換検索をした時の挙動
$(document).on('click', '.line-search-button', function() {
	station = $(this).parents('.stations-box').find('.station_service').attr("value");
	var s = "http://localhost:8000/ekimeimysql1/api/transfer/" + station + "/?format=json";
	$(".transfer-line-select").empty();

	$('.is-active').removeClass('is-active');
	$('.tab-transfer').addClass('is-active');
	$('.is-show').removeClass('is-show');
	const index = $('.tab-transfer').index();
	$('.tab-content').eq(index).addClass('is-show');

	$.getJSON(s, function(data) {
		for (var i in data) {
			var op_line = "<div value='" + data[i].line_service_pk + "' class='line-option'>" + data[i].__str__ + "</div>";
			$(".transfer-line-select").append(op_line);
		}
	})
})

//タブを切り替えた時の挙動
$(function() {
	$('.tab').click(function() {
		$('.is-active').removeClass('is-active');
		$(this).addClass('is-active');
		$('.is-show').removeClass('is-show');
		const index = $(this).index();
		$('.tab-content').eq(index).addClass('is-show');
	})
})

//駅名検索をした時の挙動
$('.namesearch').keypress(function(e) {
	if (e.which == 13) {
		namesearch();
	}
})
$('.namesearchbutton').on('click', function() {
	namesearch();
})
function namesearch() {
	text = $('.namesearch').val();
	var s = "http://localhost:8000/ekimeimysql1/api/stationsearch/" + text + "/?format=json";
	$('.station-select').empty();
	$.getJSON(s, function(data) {
		for (var i in data) {
			var op_station = "<option value='" + data[i].station_service_pk + "' data-name='" + data[i].__str__ + "' data-line='" + data[i].line_service_name + "' class='station-option'>" + data[i].__str__ + " ‐ " + data[i].line_service_name + "</option>"
			$('.station-select').append(op_station)
		}
	})
}
$(document).ready(function() {
	$('input,textarea[readonly]').not($('input[type="button"],input[type="submit"]')).keypress(function (e) {
		if (!e) var e = window.event;
		if (e.keyCode == 13) return false;
	})
})

//駅登録リスト
$(function() {
	var totalManageElement = $('input#id_stationinmovie_set-TOTAL_FORMS');
	var initialManageElement = $('input#id_stationinmovie_set-INITIAL_FORMS');
	initialManageElement.val(0);

	$(document).on('click', '.station-append', function() {
		$('.station-select option:selected').each(function() {
			station_append(this);
		})
	})

	$(document).on('dblclick', '.station-option', function() {
		station_append(this)
	})

	function station_append(station) {
		var currentFileCount = 0;
		$('.station_form').each(function() {
			currentFileCount++;
		})
		val = $(station).attr("value");
		name = $(station).data('name');
		line_name = $(station).data('line');
		// var element = "<div class='stations'><div class='stations-handle'><a class='sortable-handle'>■</a></div><div class='stations-content'><div class='stations-relation'><input type='name' name='stationinmovie_set-" + currentFileCount + "-id_in_part'id='id_stationinmovie_set-" + currentFileCount + "-id_in_part' class='id_in_part'  value='" + currentFileCount + "'><div class='stations-relation-line'></div><select name='stationinmovie_set-" + currentFileCount + "-back_rel' id='id_stationinmovie_set-" + currentFileCount + "-back_rel' class='back_rel'><option value='0'>同一駅</option><option value='1' selected='selected'>つながっている</option><option value='2'>離れている</option></select></div><div class='stations-box'><input type='checkbox' name='postvalue[]' value='" + val + "' class='station_checkbox' checked='checked'><div class='stations-info'><input type='hidden' name='stationinmovie_set-" + currentFileCount + "-station_service' id='id_stationinmovie_set-" + currentFileCount + "-station_service' class='station_service'  value='" + val + "'><div class='station-name-container'><div class='station-name-fixed'>" + name + "</div>歌唱名：<input type='name' name='stationinmovie_set-" + currentFileCount + "-station_sung_name'  value='" + name + "' id='id_stationinmovie_set-" + currentFileCount + "-station_sung_name' class='station_sung_name'></div></div><div class='line-search'><a class='line-search-button'>路線検索</a></div><div class='stations-remarks'>備考<input type='textbox' name='remarks[]' class='stations-remarks-text'></div><div class='stations-delete'><a class='sortable-delete'>削除</a></div></div></div></div>"
		var element = "<div class='stations'><div class='stations-handle'><a class='sortable-handle ui-sortable-handle'>■</a></div><div class='stations-content'><div class='stations-relation'><input type='hidden' name='stationinmovie_set-" + currentFileCount + "-id_in_part' value='" + currentFileCount + "' class='id_in_part' id='id_stationinmovie_set-" + currentFileCount + "-id_in_part'><div class='stations-relation-line'></div><div class='stations-relation-select'><select name='stationinmovie_set-" + currentFileCount + "-back_rel' class='back_rel' id='id_stationinmovie_set-" + currentFileCount + "-back_rel'><option value='0'>強制的につなげる</option><option value='1' selected='selected'>通常接続</option><option value='2'>強制的に離す</option></select></div></div><div class='stations-box'><div class='line-search'><a class='line-search-button'>路線<br> 検索</a></div><div class='stations-info'><div class='stations-info-top'><input type='hidden' name='stationinmovie_set-" + currentFileCount + "-station_service' value='" + val + "' class='station_service' id='id_stationinmovie_set-" + currentFileCount + "-station_service'><div class='station-name-container'><div class='station-name-fixed'>" + name + "</div><div class='station-remarks'>備考：<input type='textbox' name='remarks[]' class='stations-remarks-text'></div></div></div><div class='stations-info-bottom'><div class='station-sung-name'>歌唱名：<input type='text' name='stationinmovie_set-" + currentFileCount + "-station_sung_name' value='" + name + "' maxlength='50' class='station_sung_name' id='id_stationinmovie_set-" + currentFileCount + "-station_sung_name'></div><div class='line-name'>" + line_name + "</div></div></div><div class='stations-delete'><a class='sortable-delete'>削除</a></div></div></div></div>"
		$('div#file-area').append("<div class'station_form'>" + element + "</div>");
		$('div.selected-list').append("<div class='station_form'>" + element + "</div>");
		currentFileCount += 1;
		totalManageElement.attr('value', currentFileCount);
		var selectedlist = $('.selected-list');
		$(selectedlist).scrollTop(selectedlist[0].scrollHeight);
	}

	$('div.selected-list').sortable({
		handle: ".sortable-handle",
		update: function() {
			$('.station_form').each(function(i, form) {
				fields = ['id_in_part', 'movie_part', 'station_service', 'station_sung_name', 'non_line', 'back_rel']
				$(form).find('.id_in_part').val(i);
				$.each(fields,
					function(index, elem) {
						$(form).find('.' + elem).attr('name', 'stationinmovie_set-' + i + '-' + elem);
						$(form).find('.' + elem).attr('id', 'id_stationinmovie_set-' + i + '-' + elem);
					}
				)
			})
		}
	})

	$(document).on('click', '.sortable-delete', function() {
		$(this).parents(".station_form").remove();
		$('.station_form').each(function(i, form) {
			fields = ['id_in_part', 'movie_part', 'station_service', 'station_sung_name', 'non_line', 'back_rel']
			$(form).find('.id_in_part').val(i);
			$.each(fields,
				function(index, elem) {
					$(form).find('.' + elem).attr('name', 'stationinmovie_set-' + i + '-' + elem);
					$(form).find('.' + elem).attr('id', 'id_stationinmovie_set-' + i + '-' + elem);
				}
			)
		})
		var currentFileCount = 0;
		$('.station_form').each(function() {
			currentFileCount++;
		})
		var totalManageElement = $('input#id_stationinmovie_set-TOTAL_FORMS');
		totalManageElement.attr('value', currentFileCount);
	})
})