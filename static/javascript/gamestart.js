
function gamestart()
{
    var http = getXMLHttpRequest();
    if (http !== null)
    {
        http.open("GET", "/TestDebig/GameStartReal", true);
        http.onreadystatechange = function (event) {
            if (http.readyState === 4) {
                if (http.status === 200 || http.status === 0) {
                    var result = http.responseText;
                    document.getElementById("gamestart").src = result;
                    /*var errorFunc = function () {
                        alert('클라이언트가 설치되어 있지 않습니다. \n\n먼저 다운로드 페이지에서 클라이언트를 설치해주세요.');
                        window.location = "/Default/Download";
                    }
                    try {
                        var is_ie1 = navigator.userAgent.toLowerCase().indexOf('msie') > -1;
                        var is_ie2 = navigator.userAgent.toLowerCase().indexOf('trident') > -1;
                        var is_ff = navigator.userAgent.toLowerCase().indexOf('firefox') > -1;
                        var is_opera = navigator.userAgent.toLowerCase().indexOf('opera') > -1;
                        if (is_ff || is_opera)
                        {
                            ifrm = document.createElement("iframe");
                            ifrm.setAttribute("src", result);
                            ifrm.style.display = "none";
                            ifrm.onerror = errorFunc;
                            document.body.appendChild(ifrm);
                        }
                        else
                        {
                            window.setTimeout(errorFunc, 1000);
                            window.location = result;
                        }
                    } catch (err) {
                        return false;
                    }*/

                } else if (http.status === 201) {
                    var result = http.responseText;
                    alert(result);
                }
            }
        }
        http.send();
    }
    else
    {
        alert('게임 스타트가 지원되지 않습니다.');
    }
        
}

function getXMLHttpRequest() {

    var xhr = null;

    if (window.XMLHttpRequest || window.ActiveXObject) {
        if (window.ActiveXObject) {
            try {
                xhr = new ActiveXObject("Msxml2.XMLHTTP");
            } catch (e) {
                xhr = new ActiveXObject("Microsoft.XMLHTTP");
            }
        } else {
            xhr = new XMLHttpRequest();
        }
    }

    return xhr;

}
