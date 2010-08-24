/*
* Author:      Marco Kuiper (http://www.marcofolio.net/)
* BelongsTo:   The iPhone unlock screen in xHTML, CSS and jQuery
* Modifications: Swing back and "slide to unlock"-fade made by Martin Jansson (http://www.martinjansson.se)
*/

$(document).ready(function()
{
	// Set the slider to be sliding
	$("#unlock-slider").slider({
		handle: "#unlock-handle",
		animate:true,
		slide: function(e,ui)
		{
			$("#slide-to-unlock").css("opacity", 1-(parseInt($("#unlock-handle").css("left"))/120));
		},
		stop: function(e,ui)
		{
			if($("#unlock-handle").position().left == 205)
			{
				unlock();
			}
			else
			{
				$("#unlock-handle").animate({left: 0}, 200 );
				$("#slide-to-unlock").animate({opacity: 1}, 200 );
			}
		}
		}
	);
	
	var unlock = function()
	{
		//$("#iphone-inside").animate({backgroundPosition: '0 40'}, 400, '', function()
		//{
			$("#unlock-bottom").animate({bottom: -100}, 300);
			$("#unlock-top").animate({top: -100}, 300, '', function()
			{});	
			$("#iphone-inside").fadeOut("normal", function(){window.location="/servicios/";});								  
		//});
	}
	
	// Set the date and time
	var d_names = new Array("Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sabado");
	var m_names = new Array("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre");
	var d = new Date();
	var curr_day = d.getDay();
	var curr_date = d.getDate();
	var curr_month = d.getMonth();
	var curr_year = d.getFullYear();
	var curr_hour = d.getHours();
	var curr_min = d.getMinutes();
	
	$("#datepicker").replaceWith("<p class=\"date\">" + d_names[curr_day] + ", " + m_names[curr_month] + " " + curr_date + "</p>");
	
	// Adding a "0" when hours / minutes is only one character
	if(curr_hour < 10)
	{
		curr_hour = "0" + curr_hour;	
	}
	if(curr_min < 10)
	{
		curr_min = "0" + curr_min;
	}
	$("#timepicker").replaceWith("<p class=\"time\">" + curr_hour + ":" + curr_min + "</p>");
	
});
