using System;
using System.Collections.Generic;
using System.Data;
using System.Data.Entity;
using System.Linq;
using System.Net;
using System.Runtime.Remoting.Metadata.W3cXsd2001;
using System.Web;
using System.Web.Mvc;
using WebApplication1.Models;

namespace WebApplication1.Controllers
{
    public class blocksController : Controller
    {
        private RoboDbMainEntities db = new RoboDbMainEntities();

        // GET: blocks
        public ActionResult Index()
        {
            return View(db.blocks.ToList());
        }

        // GET: blocks/Details/5
        public ActionResult Details(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            block block = db.blocks.Find(id);
            if (block == null)
            {
                return HttpNotFound();
            }
            return View(block);
        }
        public ActionResult ChooseSymptom()
        {
            return View(db.Qdbs.Where(x=>x.state==-1 || x.state==1).ToList());
        }
        public ActionResult ChooseOrgan(int SympId)
        {
            return View(db.ODBs.ToList());
        }
        public ActionResult Chooseeffector(int SympId, string OrganName)
        {
            return View(db.EffectorsDbs.ToList());
        }
        // GET: blocks/Create
        public ActionResult Create(int SympId,string OrganName, int EffectoridParam, string EffectorNameParam, string EffectorTypeParam)
        {
    
            return View();
        }

        // POST: blocks/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to, for 
        // more details see https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create([Bind(Include = "")] block block, int SympId, string OrganName, int EffectoridParam, string EffectorNameParam,string EffectorTypeParam)
        {
            if (ModelState.IsValid)
            {

                block.type_effector = EffectorTypeParam;
                block.effectorName = EffectorNameParam;
                block.EffectorId = EffectoridParam;
                block.place = OrganName;
                block.SympId = SympId;
                block.blockId = db.blocks.Select(x => x.blockId).Count();
                db.blocks.Add(block);
                db.SaveChanges();
                return RedirectToAction("Index");
            }

            return View(block);
        }

        // GET: blocks/Edit/5
        public ActionResult Edit(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            block block = db.blocks.Find(id);
            if (block == null)
            {
                return HttpNotFound();
            }
            return View(block);
        }

        // POST: blocks/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to, for 
        // more details see https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit([Bind(Include = "SympId,effectorName,place,type_effector,EffectorId,blockId")] block block)
        {
            if (ModelState.IsValid)
            {
                db.Entry(block).State = System.Data.Entity.EntityState.Modified;
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            return View(block);
        }

        // GET: blocks/Delete/5
        public ActionResult Delete(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            block block = db.blocks.Find(id);
            if (block == null)
            {
                return HttpNotFound();
            }
            return View(block);
        }

        // POST: blocks/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(int id)
        {
            block block = db.blocks.Find(id);
            db.blocks.Remove(block);
            db.SaveChanges();
            return RedirectToAction("Index");
        }

        protected override void Dispose(bool disposing)
        {
            if (disposing)
            {
                db.Dispose();
            }
            base.Dispose(disposing);
        }
    }
}
