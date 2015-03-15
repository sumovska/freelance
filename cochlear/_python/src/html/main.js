

if (window.magichat === undefined) {
    log.info = console.log.bind(console);
} else {
    window.magichat.log(function(log) {
        window.log = log;
    });
}
 
function find_item_with_datatype(node, id) {
    for (var i = 0; i < node.children.length; i++) {
        var matched = find_item_with_datatype(node.children[i], id);
        if (matched) {
            return matched;
        }
    }
    if (node.getAttribute("data-type") == id) {
        return node
    }
}

function set_value(node, value) {
    if (node.getAttribute('data-type') == 'selected') {
        if (node.checked != value)
        log.info('Selected changed: [%s] %s -> %s', get_row_identifier(node), node.checked, value);
        node.checked = value;
        return;
    }
    for (var prop in node) {
        if (prop == "innerText") {
            node.innerText = value;
            break;
        }
        if (prop == "value") {
            node.value = value;
            break;
        }
    }
}

function get_row_identifier(node) {
    return get_parent_with_attribute('data-row-identifier', node);
}

function get_data_new(node) {
    return get_parent_with_attribute('data-new', node);
}

function get_data_type(node) {
    return get_parent_with_attribute('data-type', node);
} 

function get_parent_with_attribute(attr, node) {
    id = node.getAttribute(attr);
    if (id) {
        return id;
    } else {
        return get_parent_with_attribute(attr, node.parentNode);
    }
}

function set_options(node, add_new, onchange, options) {
    if (node) {
        var innerHTML = options.map(function (item) {
            return '<li><a href="#" onClick="'+onchange+'">' + item + "</a></li>";
        }).join("\n");
        if (add_new) {
            innerHTML += '<li><a href="#" onClick="window.magichat.on_click_new(get_row_identifier(this), get_data_new(this))">+ New</a></li>';
        }
        node.innerHTML = innerHTML;
    }
}

function hide_current_modal() {
    $('.modal').modal('hide');
}

function update_modal_data(modal_id, add_new, row_identifier, data) {
    var node = document.getElementById(modal_id+'_modal');
    
    node.setAttribute('data-row-identifier', row_identifier);
    for(var key in data) {
        var field = document.getElementById(modal_id+"_modal_"+key);
        if (field) {
            set_option_or_value(field, $.inArray(key, add_new) != -1, "window.magichat.on_modal_value_change('"+modal_id+"', get_data_type(this), this.value || this.text)", key, data[key]);
        } else {
            log.info('ID NOT FOUND! ' + key);
        }
    }
}

function show_modal(id, add_new, row_identifier, data) {
    log.info("Showing modal dialog for: " + id);
    update_modal_data(id, add_new, row_identifier, data);
    var jnode =$('#'+id+'_modal');
    jnode.on('hidden.bs.modal', function() { 
        jnode.off('hidden.bs.modal');
        window.magichat.on_modal_hide();
    });
    jnode.on('shown.bs.modal', function() { 
        jnode.off('shown.bs.modal');
        window.magichat.on_modal_shown();
    });
    jnode.modal();
}

if (!String.prototype.endsWith) {
    Object.defineProperty(String.prototype, 'endsWith', {
        value: function (searchString, position) {
            var subjectString = this.toString();
            if (position === undefined || position > subjectString.length) {
                position = subjectString.length;
            }
            position -= searchString.length;
            var lastIndex = subjectString.indexOf(searchString, position);
            return lastIndex !== -1 && lastIndex === position;
        }
    });
}

function set_option_or_value(node, add_new, onchange, key, value) {
    if (key.endsWith("_options")) {
        node.setAttribute('data-type', key);
        set_options(node, add_new, onchange, value);
    } else {
        node.setAttribute('data-type', key);
        node.setAttribute('onchange', onchange);
        set_value(node, value);
    }
}

function set_view(mode, allowed_new, header_template, row_template, listing) {
    var view = document.getElementById(mode);
    view.innerHTML = "<tbody><tr>" + document.getElementById(header_template).innerHTML + "</tr></tbody>";
    tbody = view.firstElementChild;
    listing.map(function (data) {
        var row = document.createElement("tr");
        row.innerHTML = document.getElementById(row_template).innerHTML;
        row.setAttribute("data-row-identifier", data.identifier);
        for (var k in data) {
            var item = find_item_with_datatype(row, k);
            if (item) {
                if (k == 'selected') {
                    set_option_or_value(item, $.inArray(k, allowed_new) != -1, "window.magichat.on_row_value_changed(get_row_identifier(this), get_data_type(this), this.checked)", k, data[k])
                } else {
                    set_option_or_value(item, $.inArray(k, allowed_new) != -1, "window.magichat.on_row_value_changed(get_row_identifier(this), get_data_type(this), this.value || this.text)", k, data[k])
                }
            }
        }
        tbody.appendChild(row);
    });
    
}

function on_error(msg) {
    document.getElementById("error_messages").innerText = msg;
}

function on_load() {
    window.magichat.set_callback('set_view', set_view);
    window.magichat.set_callback('on_error', on_error);
    window.magichat.set_callback('show_modal', show_modal);
    window.magichat.set_callback('hide_current_modal', hide_current_modal);
    window.magichat.set_callback('update_modal_data', update_modal_data);
    window.magichat.set_callback('status_listener',
            function (status, percentage) {
                map = {
                    "stuck": "stuck",
                    "connected": "connected",
                    "disconnected": "disconnected"
                };
                document.getElementById("device-status").innerText = map[status];
                document.getElementById("device-load-percentage").innerText = percentage;
            });

    window.magichat.event_onload();

    setInterval(function () {
        window.magichat.poll();
    }, 50);
}
