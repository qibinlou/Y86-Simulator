//  this part is for the tag cloud demo
$(document).ready(function() {

    var source_id = 1;
    var current_cycle = 1;
    var running = false;
    var code_index = {'pc':0,'D_index':0,'E_index':0,'M_index':0,'W_index':0}

    function load_data (data) {
        
        reg = data['reg'];
        // $("#codes").contents().find(num).addClass("highlighted-f");

        num = ".number" + code_index['pc'];
        $("#codes").contents().find(num).removeClass('highlighted-f');
        code_index['pc'] = reg[reg['pc']];
        num = ".number" + code_index['pc'];
        $("#codes").contents().find(num).addClass('highlighted-f');

        num = ".number" + code_index['D_index'];
        $("#codes").contents().find(num).removeClass('highlighted-d');
        code_index['D_index'] = reg[reg['D_index']];
        num = ".number" + code_index['D_index'];
        $("#codes").contents().find(num).addClass('highlighted-d');

        num = ".number" + code_index['E_index'];
        $("#codes").contents().find(num).removeClass('highlighted-e');
        code_index['E_index'] = reg[reg['E_index']];
        num = ".number" + code_index['E_index'];
        $("#codes").contents().find(num).addClass('highlighted-e');


        num = ".number" + code_index['M_index'];
        $("#codes").contents().find(num).removeClass('highlighted-m');
        code_index['M_index'] = reg[reg['M_index']];
        num = ".number" + code_index['M_index'];
        $("#codes").contents().find(num).addClass('highlighted-m');


        num = ".number" + code_index['W_index'];
        $("#codes").contents().find(num).removeClass('highlighted-w');
        code_index['W_index'] = reg[reg['W_index']];
        num = ".number" + code_index['W_index'];
        $("#codes").contents().find(num).addClass('highlighted-w');


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
        current_cycle = 1;
        $.getJSON("/phase",
            {"source_id" : source_id, "cycle" : current_cycle},
            load_data);
    })

    $("#start").click(function() {
        if( running == true )
        {
          $("#start img").attr("src","/static/images/play.png");
           running = false;

        }
            
        else
        {
          $("#start img").attr("src","/static/images/pause.png");
          running = true;

        }
            
        run();
    });

    function run (cycle)
    {
        if (running == false) return;
        $.getJSON("/phase",
            {"source_id" : source_id, "cycle" :current_cycle},
            function(data){
                load_data(data);
                if ( data['reg']['end'] == false )
                {
                    current_cycle++;
                    setTimeout(run, Number( speed.value ) );

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
        $.getJSON("/phase",
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
                    case 38:  speed.value = Number(speed.value) - 20; break;
                    case 40:  speed.value = Number(speed.value) + 20; break;
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
     // alert("ssss");

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
     setTimeout(getfromframe, 1000);

  })

  function getfromframe()
  {
      result = JSON.parse( hidden_frame.document.body.innerHTML );
      // alert(result);
      filelist.parentNode.children[0].innerHTML = files.files[0].name;
      source_id = result[files.files[0].name];
      // alert(source_id);
      filelist.innerHTML = "";
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
      $.getJSON("/phase",
            {"source_id" : source_id, "cycle" : current_cycle},
            load_data);


      })

  }


  $("#filelist a").click(function(){
        
      filelist.parentNode.children[0].innerHTML = $(this).html();

      source_id = $(this).attr("source_id");
      current_cycle = 1;
      cpi.innerHTML = "CPI";
      cycle.innerHTML = "Cycle";
      $.getJSON("/phase",
            {"source_id" : source_id, "cycle" : current_cycle},
            load_data);
      codes.location.assign("/getcode?source_id=" + source_id);



  })

  $("#togglememo").click(function(){
    $("#memocont").slideToggle();
  })
  $("#togglecond").click(function(){
    $("#condcode").slideToggle();
  })
  $("#togglereg").click(function(){
    $("#registers").slideToggle();
  })
  $("#toggleinfo").click(function(){
    $("#info").slideToggle();
  })
  $("#togglecodes").click(function(){
    $("#codes").fadeToggle("slow");
  })

  




})
