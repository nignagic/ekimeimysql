$(function() {
	$('.line-button').on('click', function() {
		$(this).parent().next('.station-ul').slideToggle();
	})
})

$(function() {
	$('.part-table').on('click', function() {
		$(this).next('.part-detail-container').slideToggle();
	})
	$(document).on('click', '.movie-line-name', function() {
		$(this).next('.station-ul').slideToggle();
	})
	$(document).on('click', '.all-open', function() {
		$('.part-detail-container').slideDown();
		$('.station-ul').slideDown();
	})
	$(document).on('click', '.all-close', function() {
		$('.part-detail-container').slideUp();
		$('.station-ul').slideUp();
	})
})

$(function() {
	$('.part-table').each(function(index, elem) {
		forloop = 0;
		id = $(elem).data('part_id');
		category = $(elem).data('category');
		var s = "http://localhost:8000/ekimeimysql1/api/partstation/" + id + "/?format=json";
		(function(id, category) {
			$.getJSON(s, function(data) {
				beforeline = 0;
				if (category == "駅名替え歌") {
					forloop++;
					$('.station-list-' + id).append("<h4 class='movie-line-name'>駅名替え歌</h4><ul class='station-ul station-ul-" + forloop + "'></ul>")
				}
				for (var i in data) {
					line = data[i].line_service_pk;
					if (data[i].line_service_pk != beforeline && category != "駅名替え歌") {
						forloop++;
						$('.station-list-' + id).append("<h4 class='movie-line-name'>" + data[i].line_service_name + "</h4><ul class='station-ul station-ul-" + forloop + "'></ul>")
					}
					if (category == "駅名替え歌") {
						station_text = data[i].station_sung_name + " - " + data[i].line_service_name + "[" +  data[i].pref + "]";
					} else {
						station_text = data[i].station_sung_name;
					}
					var station = "<li class='station-name'><a href='http://localhost:8000/ekimeimysql1/stationservice/" + data[i].station_service_pk + "'>" + station_text + "</a></li>";
					$('.station-ul-' + forloop).append(station)
					beforeline = line;
				}
				$('.station-list-' + id).append("</ul>")
			})
		})(id, category);
	})
})