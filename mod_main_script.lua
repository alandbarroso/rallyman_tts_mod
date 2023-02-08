--[[ Lua code. See documentation: https://api.tabletopsimulator.com/ --]]

--[[ The onLoad event is called after the game save finishes loading. --]]
function onLoad()
    testFunction()
end

--[[ The onUpdate event is called once per frame. --]]
function onUpdate()
    --[[ print('onUpdate loop!') --]]
end

function testFunction()
    local mesh_url = "https://gist.githubusercontent.com/Baryonyx6/160cef7c0ee1ca5331ab5853c09bdaa4/raw/f0015b36879f638f80533f6892814fd37617106f/holt_hex_coll.obj"

    local object = spawnObject({
        type = Custom_Model(
                mesh = mesh_url,
                diffuse 
            )
    })
end