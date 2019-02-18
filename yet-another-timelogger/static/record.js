const log = console.log.bind(console)
const e = (selector) => document.querySelector(selector)
const eall = (selector) => document.querySelectorAll(selector)

const init = () => {
    let date = new Date()
    let default_date = date.getFullYear() +
        date.getMonth() + 1 + date.getDate()
    var options = {
        "defaultDate": date,
        "autoClose": true,
        "setDefaultDate": true,
        "format": "yyyy-mm-dd"
    }
    document.addEventListener('DOMContentLoaded', function () {
        var elems = document.querySelectorAll('.datepicker')
        var instances = M.Datepicker.init(elems, options)
    })

    var time_options = {
        "twelveHour": false,
        "autoClose": true
    }

    document.addEventListener('DOMContentLoaded', function () {
        var elems = document.querySelectorAll('.timepicker');
        var instances = M.Timepicker.init(elems, time_options);
    });
}
const set_time = (origin, time) => {
    origin = origin.split(" ")[0] + " " + time
    return origin
}

const set_date = (origin, date) => {
    origin = date + " " + origin.split(" ")[1]
    return origin
}

const set_start_time = (time) => {
    let ele = e("#start_time_id")
    ele.value = set_time(ele.value, time)
}

const set_start_date = (date) => {
    let ele = e("#start_time_id")
    log(ele.value)
    ele.value = set_date(ele.value, date)
}

const set_end_time = (time) => {
    let ele = e("#end_time_id")
    ele.value = set_time(ele.value, time)
}

const set_end_date = (date) => {
    let ele = e("#end_time_id")
    log(ele.value)
    ele.value = set_date(ele.value, date)
}


const bind_event = () => {
    e("#start_date").addEventListener(
        "change", (v) => {
            if (v.target.value) {
                set_start_date(v.target.value)
            }
        }
    )
    e("#start_time").addEventListener(
        "change", (v) => {
            if (v.target.value) {
                set_start_time(v.target.value)
            }
        }
    )
    e("#end_date").addEventListener(
        "change", (v) => {
            if (v.target.value) {
                set_end_date(v.target.value)
            }
        }
    )
    e("#end_time").addEventListener(
        "change", (v) => {
            if (v.target.value) {
                set_end_time(v.target.value)
            }
        }
    )
}

const ___main = () => {
    init()
    bind_event()
}
___main()