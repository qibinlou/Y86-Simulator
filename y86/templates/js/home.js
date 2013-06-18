//  this part is for the tag cloud demo
$(document).ready(function() {

    function load_data (data) {
        reg = data['reg'];

                // for registers
                eax.innerHTML = reg['eax'];
                ecx.innerHTML = reg['ecx'];
                edx.innerHTML = reg['edx'];
                ebx.innerHTML = reg['ebx'];
                ebp.innerHTML = reg['ebp'];
                esp.innerHTML = reg['esp'];
                edi.innerHTML = reg['edi'];
                esi.innerHTML = reg['esi'];

                // for conditional codes

                cf.innerHTML = reg['CF'];
                of.innerHTML = reg['OF'];
                zf.innerHTML = reg['ZF'];
                sf.innerHTML = reg['SF'];


                pc.innerHTML = reg['pc'];


                dicode.innerHTML = reg['D_icode'];
                difunc.innerHTML = reg['D_ifunc'];
                ra.innerHTML = reg['rA'];
                rb.innerHTML = reg['rB'];
                dvalc.innerHTML = reg['D_valC'];
                dvalp.innerHTML = reg['D_valP'];

                eicode.innerHTML = reg['E_icode'];
                eifunc.innerHTML = reg['E_ifunc'];
                evalc.innerHTML = reg['E_valC'];
                evala.innerHTML = reg['E_valA'];
                evalb.innerHTML = reg['E_valB'];
                edste.innerHTML = reg['E_dstE'];
                edstm.innerHTML = reg['E_dstM'];
                srca.innerHTML = reg['srcA'];
                srcb.innerHTML = reg['srcB'];


                micode.innerHTML = reg['M_icode'];
                bch.innerHTML = reg['bch'];
                mvale.innerHTML = reg['M_valE'];
                mvalm.innerHTML = reg['M_valM'];
                mdste.innerHTML = reg['M_dstE'];
                mdstm.innerHTML = reg['M_dstM'];

                wicode.innerHTML = reg['W_icode'];
                wvale.innerHTML = reg['W_valE'];
                wvalm.innerHTML = reg['W_valM'];
                wdste.innerHTML = reg['W_dstE'];
                wdstm.innerHTML = reg['W_dstM'];


        


                console.log(data);
    }
	$("#init").click(function(){
        $.getJSON("http://localhost:8080/phase",
            {"source_id" : 1, "cycle" : 1},
            load_data);
    })

    $("#start").click(function() {
        run(1);
    });

    function run (cycle)
    {
        $.getJSON("http://localhost:8080/phase",
            {"source_id" : 1, "cycle" : cycle},
            function(data){
                load_data(data);
                if ( data['reg']['end'] == false )
                    run(cycle+1);

            });
    }

})
