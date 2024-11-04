def validate(data, template):
    state = True

    error = traverse_dict(template,data)
    if error:
        state = False

    return state, error


def traverse_dict(t_dict,d1, chain_str=''):
    
    final_chain = ''

    extra = set(d1.keys()) - set(t_dict.keys())
    if extra:
        final_chain = f"mismatched keys: {chain_str +', '.join(extra)}"
        return final_chain
    
    for key, value in t_dict.items():
        
        if key in d1.keys():  
            
            if isinstance(value, dict) and isinstance(d1[key], dict):
                err = traverse_dict(value,d1[key], chain_str+f'{key}.')
                final_chain += err
            else:
                if isinstance(d1[key],value)==False:
                    final_chain = f"bad type: {chain_str +key}"
                    return final_chain
        else:
            final_chain = f"mismatched keys: {chain_str +key}"
            return final_chain   

    return final_chain             
                 
        