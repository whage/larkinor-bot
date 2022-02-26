document.addEventListener('keydown', keydownHandler);

function keydownHandler(e) {
  switch (e.code) {
    case "ArrowRight":
      document.urlap.Submit.value='svGoEast'; document.urlap.submit();
      break;
    case "ArrowLeft":
      document.urlap.Submit.value='svGoWest'; document.urlap.submit();
      break;
    case "ArrowUp":
      document.urlap.Submit.value='svGoNorth'; document.urlap.submit();
      break;
    case "ArrowDown":
      document.urlap.Submit.value='svGoSouth'; document.urlap.submit();
      break;
    case "KeyA":
      document.urlap.Submit.value='svEngageCreature'; document.urlap.submit();
      break;
    case "KeyQ":
      document.urlap.par1.value='mag'; document.urlap.par2.value=1; document.urlap.Submit.value='svAttack'; document.urlap.submit();
      break;
    case "KeyW":
      document.urlap.par1.value='mag'; document.urlap.par2.value=2; document.urlap.Submit.value='svAttack'; document.urlap.submit();
      break;
    case "KeyE":
      document.urlap.par1.value='mag'; document.urlap.par2.value=3; document.urlap.Submit.value='svAttack'; document.urlap.submit();
      break;
    case "KeyR":
      document.urlap.par1.value='mag'; document.urlap.par2.value=4; document.urlap.Submit.value='svAttack'; document.urlap.submit();
      break;
    case "KeyC":
      document.urlap.Submit.value='svContinue'; document.urlap.submit();
      break;
  }
  console.log(` ${e.code}`)
}