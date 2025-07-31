(function()
    local WebSocketURL = "ws://127.0.0.1:51948" -- поменяй порт если ты его поменял в питоне

    local function prints(str)
        print("[AutoJoiner]: " .. str)
    end

    local function connect()
        while true do
            prints("Trying to connect to" .. WebSocketURL)
            local success, socket = pcall(WebSocket.connect, WebSocketURL)

            if success and socket then
                prints("Connected to WebSocket")
                local ws = socket

                ws.OnMessage:Connect(function(msg)
                    prints("Running the script: " .. msg)
                    local func, err = loadstring(msg)
                    if func then
                        local ok, result = pcall(func)
                        if not ok then
                            prints("Error while executing script: " .. result)
                        end
                    else
                        prints("Some unexcepted error: " .. err)
                    end
                end)

                local closed = false
                ws.OnClose:Connect(function()
                    if not closed then
                        closed = true
                        prints("The websocket closed, trying to reconnect...")
                        wait(1)
                        connect()
                    end
                end)

                break
            else
                prints("Unable to connect to websocket, trying again..")
                wait(1)
            end
        end
    end
    connect()
end)()
-- https://github.com/notasnek