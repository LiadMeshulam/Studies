variables_a = {
    "a":"a",
    "b":["a","b","c"],
    "c":["a","b"],
    "d":"ddf"
}

a = [list(map(print, suba)) for suba in variables_a]