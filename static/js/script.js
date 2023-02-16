function uploadImage() {
    const fileInput = document.getElementById("myFile");
    const uploadedImage = document.getElementById("uploadedImage");
    
    // 파일을 선택하지 않은 경우
    if (!fileInput.value) {
        return;
    }
    
    const file = fileInput.files[0];
    const reader = new FileReader();
    
    // 파일을 읽은 후 이미지를 표시
    reader.onload = function() {
      uploadedImage.src = reader.result;
    }
    
    // 이미지 파일 읽기 시작
    reader.readAsDataURL(file);
}

function test() {
    var slider = document.getElementById("myRange");
    var output = document.getElementById("value");
    output.innerHTML = slider.value;
    
    slider.oninput = function() {
        output.innerHTML = this.value;
    }
}

function form_action() {
  var form = document.getElementById("form");
  //form.action = "/";
  //form.method = "GET";
  form.submit();
}