A -> yxD | yzA | z

D -> xyzD | wxA | ε

AnaliseSintatica(){
	totalToken;
	t_A(totalToken);
}

A -> yxD | yzA | z

t_A(totalToken){
	token = totalToken.nextToken();

    if(token == 'z')
        return OK;
    else
        switch(token){
            'yx':
                t_D'(totalToken);
                break;
            'yz':
                t_A(totalToken);
                break;
            defalt:           
                return ERRO;

    }
    
}

D' -> xyzD | wxA | ε

t_D'(totalToken){
    token = totalToken.nextToken();

    if(token == 'EOF')
        return OK;

    else
        switch(token){
            'xyz':
                t_D'(totalToken);
                break;
            'wx':
                t_A(totalToken);
                break;
            default:
                return ERRO;


    }
    }




















