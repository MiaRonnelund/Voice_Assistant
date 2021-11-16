import testing

unknown_Protocol = {}

def register_protocol():
    unknown_Protocol["morning"] = testing.morning_input
    unknown_Protocol["night"] = testing.night_input
    unknown_Protocol["adds"] = testing.a_state
    unknown_Protocol["location"] = testing.l_state

if __name__ == "__main__":
    # miaProtocol = {"basic_info": True, "time": [8, 12], "goverment": True, "adds": True}

    # for key in miaProtocol:
    #     print(miaProtocol[key])

    #testing.window
    register_protocol()

    for k in unknown_Protocol:
        print(unknown_Protocol[k])