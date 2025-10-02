agent_codename = input("Agent’s Codename: ")
agent_realname = input("Agent’s Real Name: ")
gadjet = input("Assigned Gadjet: ")
mission_location = input("Mission Location: ")
operation_number = input("Operation Number: ")

# PRINTING PROCESS
print(f"""****************************************
      TOP SECRET - AGENT DOSSIER
****************************************

Codename:   {agent_codename}
Real Name:  {agent_realname}
Gadget:     {gadjet}

----------------------------------------
MISSION DETAILS:
Operation ID:   OP-{operation_number}-{agent_codename}
Location:       {mission_location}
----------------------------------------
       *** FOR YOUR EYES ONLY ***
****************************************""")