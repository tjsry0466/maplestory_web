
function HtmlDrawJobSelectBox(val) {
    var ret = "";
    if (val == -1) {
        ret += "<option value='-999'>--</option>";
    }
    else if (val == 0) {
        ret += "<option>--</option>";
        ret += "<option value='0'>전체</option>";
    }
    else if (val == 1) {
        ret += "<option>--</option>";
        ret += "<option value='-1'>전체</option>";
        ret += "<option value='100'>검사</option>";
        ret += "<option value='110'>파이터</option>";
        ret += "<option value='111'>크루세이더</option>";
        ret += "<option value='112'>히어로</option>";
        ret += "<option value='120'>페이지</option>";
        ret += "<option value='121'>나이트</option>";
        ret += "<option value='122'>팔라딘</option>";
        ret += "<option value='130'>스피어맨</option>";
        ret += "<option value='131'>용기사</option>";
        ret += "<option value='132'>다크나이트</option>";
    }
    else if (val == 2) {
        ret += "<option>--</option>";
        ret += "<option value='-2'>전체</option>";
        ret += "<option value='200'>매지션</option>";
        ret += "<option value='210'>위자드(불,독)</option>";
        ret += "<option value='211'>메이지(불,독)</option>";
        ret += "<option value='212'>아크메이지(불,독)</option>";
        ret += "<option value='220'>위자드(썬,콜)</option>";
        ret += "<option value='221'>메이지(썬,콜)</option>";
        ret += "<option value='222'>아크메이지(썬,콜)</option>";
        ret += "<option value='230'>클레릭</option>";
        ret += "<option value='231'>프리스트</option>";
        ret += "<option value='232'>비숍</option>";
    }
    else if (val == 3) {
        ret += "<option>--</option>";
        ret += "<option value='-3'>전체</option>";
        ret += "<option value='300'>아처</option>";
        ret += "<option value='310'>헌터</option>";
        ret += "<option value='311'>레인저</option>";
        ret += "<option value='312'>보우마스터</option>";
        ret += "<option value='320'>사수</option>";
        ret += "<option value='321'>저격수</option>";
        ret += "<option value='322'>신궁</option>";
    }
    else if (val == 4) {
        ret += "<option>--</option>";
        ret += "<option value='-4'>전체</option>";
        ret += "<option value='400'>로그</option>";
        ret += "<option value='410'>어쌔신</option>";
        ret += "<option value='411'>허밋</option>";
        ret += "<option value='412'>나이트로드</option>";
        ret += "<option value='420'>시프</option>";
        ret += "<option value='421'>시프마스터</option>";
        ret += "<option value='422'>섀도어</option>";
    }
    else if (val == 5) {
        ret += "<option>--</option>";
        ret += "<option value='-5'>전체</option>";
        ret += "<option value='500'>해적</option>";
        ret += "<option value='510'>인파이터</option>";
        ret += "<option value='511'>버커니어</option>";
        ret += "<option value='512'>바이퍼</option>";
        ret += "<option value='520'>건슬링거</option>";
        ret += "<option value='521'>발키리</option>";
        ret += "<option value='522'>캡틴</option>";
    }
    else if (val == 10) {
        ret += "<option>--</option>";
        ret += "<option value='-10'>전체</option>";
        ret += "<option value='1000'>노블레스</option>";
        ret += "<option value='1100'>소울마스터</option>";
        ret += "<option value='1200'>플레임위자드</option>";
        ret += "<option value='1300'>윈드브레이커</option>";
        ret += "<option value='1400'>나이트워커</option>";
        ret += "<option value='1500'>스트라이커</option>";
    }
    else if (val == 21) {
        ret += "<option>--</option>";
        ret += "<option value='-21'>전체</option>";
    }
    else if (val == 22) {
        ret += "<option>--</option>";
        ret += "<option value='-22'>전체</option>";
    }
    return ret;
}