from tkinter import *
from tkinter import ttk 
from pokeapi import get_pokemon_info


def main():
    # Create the window
    root = Tk()
    root.title("Pokemon Info Viewer")
    root.iconbitmap("pokeball.ico")
    root.resizable(False, False)
    # Create the frames
    frm_input = ttk.Frame(root)
    frm_input.grid(row=1, column=1, columnspan=2, pady=10)


    frm_stats = ttk.LabelFrame(root, text="Stats")
    frm_stats.grid(row=2, column=2, padx=10, pady=10, sticky= N)
    
    frm_info = ttk.LabelFrame(root, text="Info")
    frm_info.grid(row=2, column=1, padx=10, pady=10, sticky= N)
    
    # Populate the user input frame
    lbl_name = ttk.Label(frm_input, text='Pokemon name:')
    lbl_name.grid(row=0, column=0, padx=10, pady=10)

    ent_name = ttk.Entry(frm_input)
    ent_name.grid(row=0, column=1, pady=10)

    def btn_get_info_click():
        name = ent_name.get()
        poke_dict = get_pokemon_info(name)
        if poke_dict:
            lbl_height_val['text'] = str(poke_dict['height']) + ' dm'
            lbl_weight_val['text'] = str(poke_dict['weight']) + ' hg'
            
            types_list = [t['type']['name'] for t in poke_dict['types']]
            lbl_type_val['text'] = ', '.join(types_list)
            prg_hp['value'] = poke_dict['stats'][0]['base_stat']
            prg_attack['value'] = poke_dict['stats'][1]['base_stat']
            prg_defense['value'] = poke_dict['stats'][2]['base_stat']
            prg_special_attack['value'] = poke_dict['stats'][3]['base_stat']
            prg_special_defense['value'] = poke_dict['stats'][4]['base_stat']
            prg_speed['value'] = poke_dict['stats'][5]['base_stat']








    btn_get_info = ttk.Button(frm_input, text= 'Get info', command=btn_get_info_click)
    btn_get_info.grid(row=0, column=2, padx=10, pady=10)

    # Populate the stats frame

    lbl_hp = ttk.Label(frm_stats, text='HP:')  
    lbl_hp.grid(row=0, column=0, padx=10, pady=10, sticky=E)    
    prg_hp = ttk.Progressbar(frm_stats, length=200, maximum=255.0)
    prg_hp.grid(row=0, column=1, padx=(0,10), pady=10)

    lbl_attack = ttk.Label(frm_stats, text='Attack:')  
    lbl_attack.grid(row=1, column=0, padx=10, pady=0, sticky=E)    
    prg_attack = ttk.Progressbar(frm_stats, length=200, maximum=255.0)
    prg_attack.grid(row=1, column=1, padx=(0,10), pady= 0)

    lbl_defense = ttk.Label(frm_stats, text='Defense:')  
    lbl_defense.grid(row=2, column=0, padx=10, pady=10, sticky=E)    
    prg_defense = ttk.Progressbar(frm_stats, length=200, maximum=255.0)
    prg_defense.grid(row=2, column=1, padx=(0,10), pady=10)

    lbl_special_attack = ttk.Label(frm_stats, text='Special Attack:')  
    lbl_special_attack.grid(row=3, column=0, padx=10, pady=10, sticky=E)    
    prg_special_attack = ttk.Progressbar(frm_stats, length=200, maximum=255.0)
    prg_special_attack.grid(row=3, column=1, padx=(0,10), pady=10)

    lbl_special_defense = ttk.Label(frm_stats, text='Special Defense:')  
    lbl_special_defense.grid(row=4, column=0, padx=10, pady=10, sticky=E)    
    prg_special_defense = ttk.Progressbar(frm_stats, length=200, maximum=255.0)
    prg_special_defense.grid(row=4, column=1, padx=(0,10), pady=10)

    lbl_speed = ttk.Label(frm_stats, text='Speed:')  
    lbl_speed.grid(row=5, column=0, padx=10, pady=10, sticky=E)    
    prg_speed = ttk.Progressbar(frm_stats, length=200, maximum=255.0)
    prg_speed.grid(row=5, column=1, padx=(0,10), pady=10)

    # Populate the info frame
    lbl_height = ttk.Label(frm_info, text='Height:')
    lbl_height.grid(row=100, column=100, padx=10, pady=(10,0), sticky=E)
    lbl_height_val = ttk.Label(frm_info, width=15 )
    lbl_height_val.grid(row=100, column=200, padx=10, pady=(10,0), sticky= W)

    lbl_weight = ttk.Label(frm_info, text='Weight:')
    lbl_weight.grid(row=200, column=100, padx=10, pady=(10,0), sticky=E)
    lbl_weight_val = ttk.Label(frm_info, )
    lbl_weight_val.grid(row=200, column=200, padx=10, pady=(10,0), sticky=W)

    lbl_type = ttk.Label(frm_info, text='Type:')
    lbl_type.grid(row=300, column=100, padx=10, pady=(10,0), sticky=E)
    lbl_type_val = ttk.Label(frm_info, )
    lbl_type_val.grid(row=300, column=200, padx=10, pady=10, sticky=W)


    root.mainloop()




main()