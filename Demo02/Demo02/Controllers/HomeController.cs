using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Demo02.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace Demo02.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;

        public HomeController(ILogger<HomeController> logger)
        {
            _logger = logger;
        }

        public IActionResult Index(int codigo = 0)
        {
            ViewBag.Id = codigo;

            return View();
        }

        [Route("app/teste/{nome}/{cep:regex(^\\d{{5}}-\\d{{3}})}")]
        public IActionResult JsonTeste(string nome, string cep)
        {
            var obj = new { Nome = nome, Time = cep };

            return StatusCode(500, obj);
        }

        public IActionResult teste2()
        {
            if(DateTime.Now.Second % 2 == 0)
                return RedirectToAction("Index", new { codigo = 123 });

            return View();
        }

        public IActionResult MeuTime()
        {
            return Content("FURACAO");
        }

        public IActionResult Privacy()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
