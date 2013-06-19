//  this part is for the tag cloud demo
$(document).ready(function() {

    var source_id = 1;
    var current_cycle = 1;
    var running = false;

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
            cpi.innerHTML = "CPI:" +  (reg['total_cycle'] / reg['valid_cycle']).toFixed(2);
            cycle.innerHTML = "Cycle:" + (reg['total_cycle']-1);
            console.log(data);

        memo = data['memo'];
        memory.innerHTML = "";
        content = "";
        for( var i in memo )
        {
            content += "<tr><td>"+ i +"</td><td>"+ memo[i] +"</td></tr>";
            // console.log(content);
        }
        memory.innerHTML = content;


    }
	$("#init").click(function(){
        $.getJSON("http://localhost:8080/phase",
            {"source_id" : source_id, "cycle" : 1},
            load_data);
    })

    $("#start").click(function() {
        running = true;
        run(current_cycle);
    });

    function run (cycle)
    {
        if (running == false) return;
        $.getJSON("http://localhost:8080/phase",
            {"source_id" : source_id, "cycle" : cycle},
            function(data){
                load_data(data);
                if ( data['reg']['end'] == false )
                {
                    current_cycle++;
                    run(current_cycle);

                }
                    
            });
    }


    $("#next").click(function(){
        current_cycle++;
        gotocycle(current_cycle);

    })

    $("#back").click(function(){
        current_cycle--;
        gotocycle(current_cycle);
    })

    function gotocycle(cycle)
    {
        $.getJSON("http://localhost:8080/phase",
            {"source_id" : source_id, "cycle" : current_cycle},
            load_data);

    }

    $(document).keydown(function(e){
            //  alert(e.which);
              //  alert(movie.currentTime); 
                switch( e.which )
                {
                    case 32: if( running == true ) running = false;  else { running = true; run(current_cycle); } break;
                    case 37:  gotocycle(--current_cycle);  break;
                    case 39: gotocycle(++current_cycle); break;
                    case 38:  break;
                    case 40:  break;
                    default:break;
                }

    });

    // $('input[id=files]').change(function() {
    //     $('#photoCover').val($(this).val());
    // });


    function handleFileSelect(evt) {
    evt.stopPropagation();
    evt.preventDefault();

    var files = evt.dataTransfer.files; // FileList object.

    // files is a FileList of File objects. List some properties.
    var output = [];
    for (var i = 0, f; f = files[i]; i++) {
      output.push('<li><strong>', escape(f.name), '</strong> (', f.type || 'n/a', ') - ',
                  f.size, ' bytes, last modified: ',
                  f.lastModifiedDate.toLocaleDateString(), '</li>');
    }
    document.getElementById('list').innerHTML = '<ul>' + output.join('') + '</ul>';
  }

  function handleDragOver(evt) {
    evt.stopPropagation();
    evt.preventDefault();
    evt.dataTransfer.dropEffect = 'copy'; // Explicitly show this is a copy.
  }

  // Setup the dnd listeners.
  // var dropZone = document.getElementById('drop_zone');
  // dropZone.addEventListener('dragover', handleDragOver, false);
  // dropZone.addEventListener('drop', handleFileSelect, false);



  $(".dragresize").draggable();
  $( ".dragresize" ).resizable({
      animate: true
    });

  $("#upload").click(function(){
     len = files.files.length;
     if ( len == 0 )
     {
        alert("Please select at leaset one file!");
        return ;
     }
     for ( var i = 0; i < len; ++i )
     {
        name = files.files[i].name;
        if( name.substr(name.length-2) != "yo" )
        {
            alert("Invalid file: "+name+"\n Please select .yo files to upload!");
            return ;
        }
     }
     $("button[id=submit]").click();
     result = JSON.parse( hidden_frame.document.body.innerHTML );
     alert(result);
     filelist.parentNode.children[0].innerHTML = files.files[0].name;
     source_id = result[files.files[0].name];
     alert(source_id);
     for ( var i = 0; i < len; ++i )
     {
        name = files.files[i].name;
        filelist.innerHTML += "<li><a style='color:white;text-decoration:none;' source_id='"+ result[name] +"'>"+ name +"</a></li>";
    }
    $("#filelist a").click(function(){
        
      filelist.parentNode.children[0].innerHTML = $(this).html();

      source_id = $(this).attr("source_id");
      current_cycle = 1;
      cpi.innerHTML = "CPI";
      cycle.innerHTML = "Cycle";
      $.getJSON("http://localhost:8080/phase",
            {"source_id" : source_id, "cycle" : current_cycle},
            load_data);

     
    })


  })

  




})
