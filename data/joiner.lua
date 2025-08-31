(function()
    repeat wait() until game:IsLoaded()
    local WebSocketURL = "ws://127.0.0.1:51948" -- поменяй порт если ты его поменял в питоне

    local function prints(str)
        print("[AutoJoiner]: " .. str)
    end


    local function findTargetGui()
        for _, gui in ipairs(game:GetService('CoreGui'):GetChildren()) do
            if gui:IsA('ScreenGui') then
                if gui:FindFirstChild('Job-ID Input', true) then
                    return gui
                end
            end
        end
        return nil
    end

    local function setJobIDText(targetGui, text)
        local jobFrame = targetGui:FindFirstChild('Job-ID Input', true)
        if not jobFrame then return nil end

        local inputFrame = jobFrame:FindFirstChild('InputFrame', true)
        if not inputFrame then return nil end

        local inputBox = inputFrame:FindFirstChild('InputBox', true)
        if inputBox and inputBox:IsA('TextBox') then
            inputBox.Text = text
            prints('Textbox updated: ' .. text .. ' (10m+ bypass)')
            return inputBox
        end
        return nil
    end

    local function clickJoinButton(targetGui)
        local joinFrame = targetGui:FindFirstChild('Join Job-ID', true)
        if not joinFrame then return nil end
        return joinFrame:FindFirstChildWhichIsA('TextButton', true)
    end

    local function bypass10M(jobId)
        local targetGui = findTargetGui()
        setJobIDText(targetGui, jobId)
        local button = clickJoinButton(targetGui)

        task.defer(function()
            task.wait(0.05) -- поменяй под свое значение (если убрать = будут нули)
            for _, conn in ipairs(getconnections(button.MouseButton1Click)) do
                conn:Fire()
            end
            prints('Join server clicked (10m+ bypass)')
        end)
    end


    local function justJoin(script)
        local func, err = loadstring(script)
        if func then
            local ok, result = pcall(func)
            if not ok then
                prints("Error while executing script: " .. result)
            end
        else
            prints("Some unexcepted error: " .. err)
        end
    end


    local function connect()
        while true do
            prints("Trying to connect to " .. WebSocketURL)
            local success, socket = pcall(WebSocket.connect, WebSocketURL)

            if success and socket then
                prints("Connected to WebSocket")
                local ws = socket

                ws.OnMessage:Connect(function(msg)
                    if not string.find(msg, "TeleportService") then
                        prints("Bypassing 10m server: " .. msg)
                        bypass10M(msg)
                    else
                        prints("Running the script: " .. msg)
                        justJoin(msg)
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
-- https://github.com/notasnek/roblox-autojoiner
-- please star my repo