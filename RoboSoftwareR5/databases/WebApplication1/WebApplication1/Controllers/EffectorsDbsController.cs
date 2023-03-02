using System;
using System.Collections.Generic;
using System.Data;
using System.Data.Entity;
using System.Linq;
using System.Net;
using System.Web;
using System.Web.Mvc;
using WebApplication1.Models;

namespace WebApplication1.Controllers
{
    public class EffectorsDbsController : Controller
    {
        private RoboDbMainEntities db = new RoboDbMainEntities();

        // GET: EffectorsDbs
        public ActionResult Index()
        {
            return View(db.EffectorsDbs.ToList());
        }

        // GET: EffectorsDbs/Details/5
        public ActionResult Details(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            EffectorsDb effectorsDb = db.EffectorsDbs.Find(id);
            if (effectorsDb == null)
            {
                return HttpNotFound();
            }
            return View(effectorsDb);
        }

        // GET: EffectorsDbs/Create
        public ActionResult Create()
        {
            return View();
        }

        // POST: EffectorsDbs/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to, for 
        // more details see https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create([Bind(Include = "effectorName,effectorType")] EffectorsDb effectorsDb)
        {
            if (ModelState.IsValid)
            {
                effectorsDb.Id = db.EffectorsDbs.Count();
                db.EffectorsDbs.Add(effectorsDb);
                db.SaveChanges();
                return RedirectToAction("Index");
            }

            return View(effectorsDb);
        }

        // GET: EffectorsDbs/Edit/5
        public ActionResult Edit(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            EffectorsDb effectorsDb = db.EffectorsDbs.Find(id);
            if (effectorsDb == null)
            {
                return HttpNotFound();
            }
            return View(effectorsDb);
        }

        // POST: EffectorsDbs/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to, for 
        // more details see https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit([Bind(Include = "Id,effectorName,effectorType")] EffectorsDb effectorsDb)
        {
            if (ModelState.IsValid)
            {
                db.Entry(effectorsDb).State = System.Data.Entity.EntityState.Modified;
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            return View(effectorsDb);
        }

        // GET: EffectorsDbs/Delete/5
        public ActionResult Delete(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            EffectorsDb effectorsDb = db.EffectorsDbs.Find(id);
            if (effectorsDb == null)
            {
                return HttpNotFound();
            }
            return View(effectorsDb);
        }

        // POST: EffectorsDbs/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(int id)
        {
            EffectorsDb effectorsDb = db.EffectorsDbs.Find(id);
            db.EffectorsDbs.Remove(effectorsDb);
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
