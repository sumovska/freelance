/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	/* Forms */
	$('input, select').styler();

	/* Project tabs */
	$('.projects').each(function () {
		$('.triggers li a', this).click(function () {
			var where = $(this).attr("href").replace(/^.*#(.*)/, "$1");
			$(this).closest('li').addClass('active').siblings('li.active').removeClass('active');
			$('.tab-' + where).removeClass('tab-hidden').siblings('.tab').addClass('tab-hidden');
			return false;
		});
	});

	/* Popup script */
	$('.fancybox-popup').fancybox({
		padding: 0,
		helpers: {
			overlay: {
				speedIn: 250,
				css: {
					'background': 'rgba(0, 0, 0, 0.8)'
				}
			}
		}
	});

	$('.file-uploader').each(function () {
		var _self = $(this);
		var holder = document.getElementById('holder'),
			tests = {
				filereader: typeof FileReader != 'undefined',
				dnd: 'draggable' in document.createElement('span'),
				formdata: !!window.FormData,
				progress: "upload" in new XMLHttpRequest
			},
			support = {
				filereader: document.getElementById('filereader'),
				formdata: document.getElementById('formdata')
			},
			acceptedTypes = {
				'image/png': false,
				'image/jpeg': true,
				'image/gif': false
			},
			fileupload = document.getElementById('upload');

		$('.default', _self).click(function () {
			$('.upload', _self).removeClass('hidden');
			$(holder).addClass('hidden');
			return false;
		});

		$(".filereader, .formdata", _self).each(function (api) {
			if (tests[api] === false) {
				support[api].className = 'fail';
			} else {
				// FFS. I could have done el.hidden = true, but IE doesn't support
				// hidden, so I tried to create a polyfill that would extend the
				// Element.prototype, but then IE10 doesn't even give me access
				// to the Element object. Brilliant.
				support[api].className = 'hidden';
			}
		});

		if ($.browser.msie && $.browser.version < 10) {
			$('.upload', _self).each(function () {
				$(this).removeClass('hidden');
			});
			$(holder).addClass('hidden');
		}

		function previewfile(file) {
			if (tests.filereader === true && acceptedTypes[file.type] === true) {
				var reader = new FileReader();
				reader.onload = function (event) {
					var image = new Image();
					image.src = event.target.result;
					image.width = 250; // a fake resize
					holder.appendChild(image);
					$(holder).addClass('loaded');
					$('.submit', _self).show();
				};
				reader.readAsDataURL(file);
			} else {
				if (acceptedTypes[file.type] === true) {
					holder.innerHTML += '<p>Загружено ' + file.name + ' ' + (file.size ? (file.size / 1024 | 0) + 'K' : '');
				} else {
					holder.innerHTML += '<p class="error">Неподдерживаемый формат файла</p>';
				}
			}
		}

		function readfiles(files) {
			debugger;
			var formData = tests.formdata ? new FormData() : null;
			for (var i = 0; i < files.length; i++) {
				if (tests.formdata) formData.append('file', files[i]);
				previewfile(files[i]);
			}

			// now post a new XHR request
			if (tests.formdata) {
				var xhr = new XMLHttpRequest();
				xhr.open('POST', '/devnull.php');

				if (tests.progress) {
					xhr.upload.onprogress = function (event) {
						if (event.lengthComputable) {
							var complete = (event.loaded / event.total * 100 | 0);
						}
					}
				}

				xhr.send(formData);
			}
		}

		if (tests.dnd) {
			holder.ondragover = function () {
				$(this).addClass('hover');
				return false;
			};
			holder.ondragend = function () {
				$(this).removeClass('hover');
				return false;
			};
			holder.ondrop = function (e) {
				$(this).removeClass('hover');
				e.preventDefault();
				readfiles(e.dataTransfer.files);
			}
		} else {
			fileupload.querySelector('input').onchange = function () {
				readfiles(this.files);
			};
		}
	});

	/* IE fixes */
	if ($.browser.msie && $.browser.version < 10) {
		if ($.browser.version < 9) {
			$('body').addClass('ie8');
		}
		if (window.PIE) {
			$('.prizes .item .user, .prizes .item .user .photo').each(function () {
				PIE.attach(this);
			});
		}
		$("input[type='text'], input[type='password']").each(function () {
			$(this).val($(this).attr('placeholder'));
			$(this).focus(function () {
				if ($(this).val() === $(this).attr('placeholder')) {
					$(this).val('');
				}
			});
			$(this).blur(function () {
				if ($(this).val() === '') {
					$(this).val($(this).attr('placeholder'));
				}
			});
		});
	}
});