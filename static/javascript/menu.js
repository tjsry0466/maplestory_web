$(document).ready(function () {
    //상단 메뉴
    $('#topMenu .depth .li1, #topMenu .depth .li2, #topMenu .depth .li3, #topMenu .depth .li4, #topMenu .depth .li5').mouseover(function () { $('#topMenu .depth').addClass('depth_up'); return false; });
    $('#topMenu .depth .li1, #topMenu .depth .li2, #topMenu .depth .li3, #topMenu .depth .li5, #topMenu .depth .li5').mouseleave(function () { $('#topMenu .depth').removeClass().addClass('depth'); return false });

    $('#topMenu .depth .li1').mouseover(function () { $('#topMenu .news').show(''); return false; });
    $('#topMenu .depth .li1').mouseleave(function () { $('#topMenu .news').hide(''); return false; });

    $('#topMenu .depth .li2').mouseover(function () { $('#topMenu .guide').show(''); return false; });
    $('#topMenu .depth .li2').mouseleave(function () { $('#topMenu .guide').hide(''); return false; });

    $('#topMenu .depth .li3').mouseover(function () { $('#topMenu .ranking').show(''); return false; });
    $('#topMenu .depth .li3').mouseleave(function () { $('#topMenu .ranking').hide(''); return false; });

    $('#topMenu .depth .li4').mouseover(function () { $('#topMenu .community').show(''); return false; });
    $('#topMenu .depth .li4').mouseleave(function () { $('#topMenu .community').hide(''); return false; });

    $('#topMenu .depth .li5').mouseover(function () { $('#topMenu .policy').show(''); return false; });
    $('#topMenu .depth .li5').mouseleave(function () { $('#topMenu .policy').hide(''); return false; });

    //탭 메뉴
    var startup = Math.ceil(Math.random() * 3);
    var idnam = "news_" + startup;
    $('.news_tab>li')
        .click(
        function () {
            $('.news_tab>li')
                .removeClass('selected');
            $(this).addClass('selected');
            $('.news_tabcon>li')
                .hide();
            $('.news_tabcon>li:eq(' + $('.news_tab>li').index(this) + ')')
                .show();
            if (togglerID > 0) { //탭 메뉴 자동 전환이 활성화 되어있다면 중지
                clearInterval(togglerID);
            }
            return false;
        });
    $('.ucc_tab>li').click(function () { $('.ucc_tab>li').removeClass('selected'); $(this).addClass('selected'); $('.ucc_tabcon>li').hide(); $('.ucc_tabcon>li:eq(' + $('.ucc_tab>li').index(this) + ')').show(); return false; });

    //탭 메뉴 자동 전환
    var i = 0;
    var togglerID = 0;

    $(function () {
        togglerID = setInterval(function () {
            i = ++i % 3;
            $("#news_tab_" + (i > 0 ? (i-1) : 2)).removeClass('selected');
            $("#news_tab_" + i).addClass('selected');
            $('.news_tabcon>li')
                .hide();
            $('.news_tabcon>li:eq(' + i + ')')
                .show();
        }, 3000);
    })

    //포커스 배너
    focusRollPlay();

    //포커스 재생, 정지
    $('.focus .btn_play').click(function () { if (!$('.focus .btn_play').hasClass('play')) { $(this).addClass('play'); focusRollPlay(); } else { $(this).removeClass('play'); focusRollStop(); } });

    //포커스 숫자 카운트
    var focusCnt = $('.focus .banner>li').length;
    var focusIndex = 1;
    $('.focus .cnt').append('<em>' + focusIndex + '</em><span>/</span>' + focusCnt);

    //포커스 좌우 버튼
    $('.focus .btn_prev').click(function () { focusPrev(); focusRollStop(); $('.focus .btn_play').removeClass('play'); });
    $('.focus .btn_next').click(function () { focusNext(); focusRollStop(); $('.focus .btn_play').removeClass('play'); });

    //포커스
    function onlyFirstFocus() { $('.focus .banner>li').hide().eq(0).show(); }

    function focusPrev() { $('.focus .banner>li:last').prependTo('.focus .banner'); onlyFirstFocus(); focusIndex--; if (focusIndex <= 0) { focusIndex = focusCnt; } focusCntEmp(focusIndex); }
    function focusNext() { $('.focus .banner>li:first').appendTo('.focus .banner'); onlyFirstFocus(); focusIndex++; if (focusIndex > focusCnt) { focusIndex = 1; } focusCntEmp(focusIndex); }

    function focusCntEmp(curIndex) { $('.focus .cnt').empty(); focusCurIndex(curIndex); }
    function focusCurIndex(curIndex) { $('.focus .cnt').append('<em>' + curIndex + '</em><span>/</span>' + focusCnt); }

    function focusRollStop() { $('.btn_play').css('background-position', '0 bottom'); clearTimeout(focus_roll); }
    function focusRollPlay() { $('.btn_play').css('background-position', '0 top'); focus_roll = setInterval(function () { focusNext(); }, 3000); }

	$(function () {	 
		$(".selectbox").selectbox();	
        $(".job_class").selectbox();
        $(".purchase_method").selectbox();
		$(".sub_job").selectbox();
		$(".tag").selectbox();
	});
	$(".job_class").change(function() {
		var job_class = $(".job_class option:selected").val();
		switch(job_class){
			case "1": //모험가
				
				break;
			case "2": //시그너스
				
				break;
			case "3": //영웅
				break;
		}
	});
	$("#all_check").click(function() { checkAll(); });
	
	function checkAll() {
		var chk_status = $("input:checkbox[id='all_check']").is(":checked");
		if (chk_status) {
			$("input:checkbox[name='chk_box']").prop("checked", true);
		} else {
			$("input:checkbox[name='chk_box']").prop("checked", false);
		}
	}
});